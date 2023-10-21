#!/usr/bin/python3

import os, requests, time
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from rich.table import Table
from rich.console import Console

from utils.utils import *
from utils.configs import *
from utils.utils_http import *
from utils.utils_files import *

session = requests.Session()
console = Console(record=True)
session.headers["User-Agent"] = Configs.DEFAULT_USER_AGENT.value

def download_resources(url, resource_type, minify_files=None, filter_data=None):
    start_time = time.time()
    domain = get_hostname(url)
    path = f"download/{domain}/{resource_type}/"
    
    create_folder(path)
    
    html = session.get(url).content
    soup = bs(html, "html.parser")
    
    table = Table(box=None)
    table.add_column("Filename", style="cyan")
    table.add_column("URL", style="bold green")
    table.add_column("Size", style="blue")
    table.add_column("Status")
    
    links = extract_links(
        url, 
        soup, 
        resource_type, 
        minify_files, 
        filter_data
    )
    
    total_files = 0
    for link in list(set(links)):
        file_name = path + get_remote_file_size(link)
        content = session.get(link).content if resource_type == 'images' else session.get(link).text
        
        with open(file_name, 'wb' if resource_type == 'images' else 'w', encoding="utf-8") as f:
            f.write(content)
            
        total_files += 1
        status = "[bold green]Download completed[/bold green]" if os.path.exists(file_name) else "[bold red]Download failed[/bold red]"
        
        table.add_row(
            get_remote_file_size(link), link, local_file_size(file_name), status
        )
    
    os.startfile(
        os.path.realpath(path)
    )
    
    end_time = "{:.2f}".format(time.time() - start_time)
    table.caption = f"Total of downloaded files: {total_files} - Time taken: {end_time} seconds"
    console.print(table)

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
            
            if filter_data and not find(link, filter_data):
                continue
            
            if filter_str and not find(link, filter_str):
                continue
            
            links.append(link)
            
    return links
