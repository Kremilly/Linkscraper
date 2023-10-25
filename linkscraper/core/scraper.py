#!/usr/bin/python3

import re, requests, time

from bs4 import BeautifulSoup as bs

from utils.url import URL
from utils.http import HTTP
from layout.table import Table

def get_links(url, external_links, status_code, filter_data):
    start_time = time.time()
    
    reqs = requests.get(url).text
    soup = bs(reqs, 'html.parser')
    
    if status_code:
        headers = [
            ("Domain", "cyan", True),
            ("URL", "bold blue", False),
            ("Status", "bold", False)
        ]
    else:
        headers = [
            ("Domain", "cyan", True),
            ("URL", "bold blue", False)
        ]
    
    Table.header(headers)
    
    links = []
    
    for link in soup.find_all('a'):
        if link.get('href') != None:
            if filter_data:
                if URL.is_url(link.get('href')) and link.get('href').find(filter_data) != -1:
                    links.append(link.get('href'))
            else:
                if not external_links:
                    if URL.is_url(link.get('href')):
                        links.append(link.get('href'))
                else:
                    if URL.is_url(link.get('href')) and HTTP.get_hostname(link.get('href')).find(HTTP.get_hostname(url)) == -1:
                        links.append(link.get('href'))
    
    links_list = list(set(links))
    
    for link in list(set(links)):
        if status_code:
            Table.row(HTTP.get_hostname(link), link, HTTP.code(link))
        else:
            Table.row(HTTP.get_hostname(link), link)

    end_time = "{:.2f}".format(time.time() - start_time)
    
    Table.caption(f"Total of links in page: {len(links_list)} - Time taken: {end_time} seconds")
    Table.display()

def get_emails(url, filter_data):
    start_time = time.time()
    text = requests.get(url).text
    
    soup = str(
        bs(text,'html.parser').body
    )
    
    Table.header([
        ("Domain", "cyan", True),
        ("Email", "bold blue", False)
    ])
    
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', soup)
    list_emails = list(set(emails))
    
    for email in list_emails:
        if filter_data:
            if email.find(filter_data):
                Table.row(email.split('@')[1], email)
        else:
            Table.row(email.split('@')[1], email)
    
    end_time = "{:.2f}".format(time.time() - start_time)
    
    Table.caption(f"Total of emails on page: {len(list_emails)} - Time taken: {end_time} seconds")
    Table.display()
