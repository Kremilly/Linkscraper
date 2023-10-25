#!/usr/bin/python3

import os, requests, time
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from utils.file import File
from utils.file_ext import FileExt
from classes.configs import Configs

from layout.table import Table
from layout.layout import Layout

from utils.http import HTTP
from utils.file_size import FileSize

session = requests.Session()
session.headers["User-Agent"] = Configs.DEFAULT_USER_AGENT.value

def download_resources(url, resource_type, minify_files=None, filter_data=None):
    start_time = time.time()
    domain = HTTP.get_hostname(url)
    path = f"download/{domain}/{resource_type}/"
    
    File.create_path(path)
    
    html = session.get(url).content
    soup = bs(html, "html.parser")
    
    Table.header([
        ("Filename", "cyan", True),
        ("URL", "bold blue", False),
        ("Size", "green", False),
        ("Status", "white", False),
    ])
    
    links = extract_links(
        url, 
        soup, 
        resource_type, 
        minify_files, 
        filter_data
    )
    
    total_files = 0
    for link in list(set(links)):
        if FileExt.is_valid(File.get_remote_file_name(link)):
            file_name = path + File.get_remote_file_name(link)
            content = session.get(link).content if resource_type == 'images' else session.get(link).text
            
            try:
                mode = 'wb' if resource_type == 'images' else 'w'
                File.write(file_name, content, mode, 'utf-8')
            except PermissionError:
                Layout.error(f"Permission denied when trying to write to: {file_name}", False, True)
            
            total_files += 1
            status = "[bold green]Download completed[/bold green]" if os.path.exists(file_name) else "[bold red]Download failed[/bold red]"
            
            Table.row(
                File.get_remote_file_name(link), link, FileSize.local_file(file_name), status
            )
    
    File.open(path)
    
    end_time = "{:.2f}".format(time.time() - start_time)
    Table.caption(f"Total of downloaded files: {total_files} - Time taken: {end_time} seconds")
    Table.display()

def extract_links(url, soup, resource_type, minify_files, filter_data):
    links = []
    
    if resource_type == 'js':
        tags = soup.find_all("script")
        attr_name = "src"
        filter_str = ".min" if minify_files == "true" else None
    
    elif resource_type == 'css':
        tags = soup.find_all("link")
        attr_name = "href"
        filter_str = ".min.css" if minify_files == "true" else ".css"
        
    elif resource_type == 'images':
        tags = soup.find_all("img")
        attr_name = "src"
        filter_str = None
        
    else:
        raise ValueError(f"Unsupported resource type: {resource_type}")
    
    for tag in tags:
        if tag.attrs.get(attr_name):
            link = urljoin(
                url, tag.attrs.get(attr_name)
            )
            
            if not filter_data == None:
                if filter_data and not link.find(filter_data):
                    continue
                
                if filter_str and not link.find(filter_data):
                    continue
            
            links.append(link)

    return links
