#!/usr/bin/python3

import requests, time

from utils.utils import *
from rich.table import Table
from rich.console import Console

console = Console(record=True)

def get_cookies(url, filter_data=None):
    start_time = time.time()
    response = requests.get(url)
    
    table = Table(box=None)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value")
    
    cookie_dict = response.cookies.get_dict()
    
    if filter_data:
        cookie_dict = {k: v for k, v in cookie_dict.items() if find(k, filter_data)}

    for name, value in cookie_dict.items():
        table.add_row(name, value)

    end_time = "{:.2f}".format(time.time() - start_time)
    table.caption = f"Total of cookies on page: {len(cookie_dict)} - Time taken: {end_time} seconds"
    console.print(table)
