#!/usr/bin/python3

import requests, time

from utils.http import HTTP
from layout.table import Table

from apis.apis import Apis

class IPLocation:
    
    @classmethod
    def ip_data(cls, data):
        response = requests.get(f"{Apis.IP_API_REQUEST.value}")
        resp_json = response.json()
        return resp_json[data]

    @classmethod
    def run(cls, url):
        start_time = time.time()
        ip = HTTP.get_ip(url)
        
        response = requests.get(f"{Apis.IP_API_REQUEST.value}{ip}")
        resp_json = response.json()

        Table.header([
            ("Name", "cyan", True),
            ("Value", "white", False)
        ])

        for data in resp_json:
            if resp_json[data] != '':
                Table.row(data, str(resp_json[data]))
                
        end_time = "{:.2f}".format(time.time() - start_time)
        
        Table.caption(f"Time taken: {end_time} seconds")
        Table.display()
