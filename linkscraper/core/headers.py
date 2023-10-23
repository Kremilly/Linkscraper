#!/usr/bin/python3

import requests, time
from utils.utils import *

from rich.json import JSON
from layout.table import Table

def get_headers(url, filter_data=None):
    start_time = time.time()

    response = requests.get(url)
    headers_dict = response.headers

    if filter_data:
        headers_dict = {k: v for k, v in headers_dict.items() if find(k, filter_data)}
    
    Table.header([
        ("Name", "cyan", True),
        ("Value", "white", False)
    ])

    for header_name, header_value in headers_dict.items():
        formatted_value = JSON(header_value) if is_json(header_value) else header_value
        Table.row(header_name, formatted_value)

    end_time = "{:.2f}".format(time.time() - start_time)
    Table.caption(f"Total of headers: {len(headers_dict)} - Time taken: {end_time} seconds")
    Table.display()
