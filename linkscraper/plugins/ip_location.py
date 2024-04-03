#!/usr/bin/python3

import requests, time

from layout.table import Table

from helper.apis import Apis

from utils.http import HTTP
from utils.date_time import DateTime

class IPLocation:
    
    @classmethod
    def ip_data(cls, data):
        response = requests.get(f'{Apis.IP_API_REQUEST.value}')
        return response.json()[data]

    @classmethod
    def run(cls, url):
        start_time = time.time()
        ip = HTTP.get_ip(url)
        
        response = requests.get(f'{Apis.IP_API_REQUEST.value}{ip}')
        resp_json = response.json()

        Table.header([
            ('Name', 'cyan', True),
            ('Value', 'white', False)
        ])

        for data in resp_json:
            if resp_json[data] != '':
                Table.row(data, str(resp_json[data]))
        
        Table.caption(f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        Table.display()
