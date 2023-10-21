#!/usr/bin/python3

import requests, time

from utils.utils import *
from utils.configs import *
from utils.utils_http import *
from utils.utils_files import *
from core.download_resources import *

from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from rich.table import Table
from rich.console import Console

session = requests.Session()
console = Console(record=True)
session.headers["User-Agent"] = Configs.DEFAULT_USER_AGENT.value

def js_files(url, minify_files, filter_data, download):
    if download == "true":
        download_resources(url, 'js', minify_files, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
        
        table = Table(box=None)
        table.add_column("Filename", style="cyan")
        table.add_column("URL", style="bold green")

        links = []
        
        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                script_url = urljoin(url, script.attrs.get("src"))
                
                if filter_data:
                    if find(script_url, filter_data):
                        links.append(script_url)
                else:
                    if minify_files == "true":
                        if find(script_url, '.min'):
                            links.append(script_url)
                    else:
                        links.append(script_url)
        
        list_scripts = list(set(links))
        
        for script_url in list_scripts:
            table.add_row(get_remote_file_size(script_url), script_url)
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Total script files on page: {len(list_scripts)} - Time taken: {end_time} seconds"
        console.print(table)

def css_files(url, minify_files, filter_data, download):
    if download == "true":
        download_resources(url, 'css', minify_files, filter_data)
    else:
        start_time = time.time()
        
        html = session.get(url).content
        soup = bs(html, "html.parser")
        
        table = Table(box=None)
        table.add_column("Filename", style="cyan")
        table.add_column("URL", style="bold green")

        links = []
        
        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                css_url = urljoin(url, css.attrs.get("href"))

                if filter_data:
                    if find(css_url, ".css") and find(css_url, filter_data):
                        links.append(css_url)
                else:
                    if minify_files == "true":
                        if find(css_url, ".css") and find(css_url, ".min.css"):
                            links.append(css_url)
                    else:
                        if find(css_url, ".css"):
                            links.append(css_url)
        
        list_css = list(set(links))
        
        for css_url in list_css:
            table.add_row(get_remote_file_size(css_url), css_url)
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Total CSS files on page: {len(list_css)} - Time taken: {end_time} seconds"
        console.print(table)
    
def images_files(url, filter_data, download):
    if download == "true":
        download_resources(url, 'images', None, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
        
        table = Table(box=None)
        table.add_column("Filename", style="cyan")
        table.add_column("URL", style="bold green")

        links = []
        
        for img in soup.find_all("img"):
            img_url = urljoin(url, img.attrs.get("src"))
            
            if filter_data:
                if find(img_url, filter_data):
                    links.append(img_url)
            else:
                links.append(img_url)
    
        list_images = list(set(links))
    
        for img_url in list_images:
            table.add_row(get_remote_file_size(img_url), img_url)
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Total images files on page: {len(list_images)} - Time taken: {end_time} seconds"
        console.print(table)
