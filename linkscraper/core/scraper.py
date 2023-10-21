#!/usr/bin/python3

import re, requests, time

from utils.utils import *
from utils.utils_http import *
from utils.utils_files import *

from bs4 import BeautifulSoup as bs

from rich.table import Table
from rich.console import Console

console = Console(record=True)

def get_links(url, external_links, status_code, filter_data):
    start_time = time.time()
    
    reqs = requests.get(url).text
    soup = bs(reqs, 'html.parser')
    
    table = Table(box=None)
    table.add_column("Domain", style="cyan")
    table.add_column("URL", style="bold green")
    
    if status_code == "true":
        table.add_column("Status", style="bold")
    
    links = []
    
    for link in soup.find_all('a'):
        if link.get('href') != None:
            if filter_data:
                if is_url(link.get('href')) and find(link.get('href'), filter_data):
                    links.append(link.get('href'))
            else:
                if not external_links or external_links != "true":
                    if is_url(link.get('href')):
                        links.append(link.get('href'))
                else:
                    if is_url(link.get('href')) and find(get_hostname(link.get('href')), get_hostname(url)) != True:
                        links.append(link.get('href'))
    
    links_list = list(set(links))
    
    for link in list(set(links)):
        if status_code == "true":
            table.add_row(get_hostname(link), link, str(http_code(link)))
        else:
            table.add_row(get_hostname(link), link)

    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total of links in page: {len(links_list)} - Time taken: {end_time} seconds"
    console.print(table)

def get_emails(url, filter_data):
    start_time = time.time()
    text = requests.get(url).text
    
    soup = str(
        bs(text,'html.parser').body
    )
    
    table = Table(box=None)
    table.add_column("Domain", style="cyan")
    table.add_column("Email", style="bold blue")
    
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', soup)
    list_emails = list(set(emails))
    
    for email in list_emails:
        if filter_data:
            if find(email, filter_data):
                table.add_row(email.split('@')[1], email)
        else:
            table.add_row(email.split('@')[1], email)
    
    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total of emails on page: {len(list_emails)} - Time taken: {end_time} seconds"
    console.print(table)
