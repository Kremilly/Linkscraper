#!/usr/bin/python3

import requests, time

from utils.http import HTTP
from layout.table import Table

from apis.apis import Apis

def plugin_ip_location(url):
    ip = HTTP.get_ip(url)
    start_time = time.time()
    
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
