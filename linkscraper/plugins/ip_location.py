#!/usr/bin/python3

import requests, time

from layout.table import Table
from utils.utils_http import get_ip

def plugin_ip_location(url):
    ip = get_ip(url)
    start_time = time.time()
    
    response = requests.get(f"http://ip-api.com/json/{ip}")
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
