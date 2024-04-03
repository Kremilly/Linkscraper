#!/usr/bin/python3

import re, requests, time

from bs4 import BeautifulSoup as bs

from utils.url import URL
from utils.http import HTTP
from utils.date_time import DateTime

from layout.table import Table
from layout.layout import Layout

class Scraper:

    @classmethod
    def get_links(cls, url, external_links, status_code, filter_data):
        start_time = time.time()
        
        reqs = requests.get(url).text
        soup = bs(reqs, 'html.parser')
        
        headers = [
            ('Domain', 'cyan', True),
            ('URL', 'bold blue', False)
        ]
        
        if status_code:
            headers = [
                ('Domain', 'cyan', True),
                ('URL', 'bold blue', False),
                ('Status', 'bold', False)
            ]
        
        Table.header(headers)
        
        links = []
        
        for link in soup.find_all('a'):
            if link.get('href') != None:
                if filter_data:
                    if URL.is_url(link.get('href')) and link.get('href').find(filter_data) != -1:
                        links.append(link.get('href'))
                    
                if not external_links:
                    if URL.is_url(link.get('href')):
                        links.append(link.get('href'))
                    
                if URL.is_url(link.get('href')) and HTTP.get_hostname(link.get('href')).find(HTTP.get_hostname(url)) == -1:
                    links.append(link.get('href'))
        
        links_list = list(set(links))
        
        for link in list(set(links)):
            if status_code:
                Table.row(HTTP.get_hostname(link), link, HTTP.code(link))
                
            Table.row(HTTP.get_hostname(link), link)

        Table.caption(f'Total of links in page: {len(links_list)} - '
                      f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        
        Table.display()

    @classmethod
    def get_emails(cls, url, filter_data):
        start_time = time.time()
        text = requests.get(url).text
        
        soup = str(
            bs(text,'html.parser').body
        )
        
        Table.header([
            ('Domain', 'cyan', True),
            ('Email', 'bold blue', False)
        ])
        
        emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', soup)
        list_emails = list(set(emails))
        
        for email in list_emails:
            if filter_data:
                if email.find(filter_data):
                    Table.row(email.split('@')[1], email)
                
            Table.row(email.split('@')[1], email)

        Table.caption(f'Total of emails on page: {len(list_emails)} - '
                      f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        
        Table.display()

    @classmethod
    def section_links(cls, url, external_links, status_code, filter_data):
        Layout.header_section('Links')
        cls.get_links(url, external_links, status_code, filter_data)

    @classmethod
    def section_emails(cls, url, filter_data):
        Layout.header_section('Emails')
        cls.get_emails(url, filter_data)
