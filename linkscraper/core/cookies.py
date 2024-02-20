#!/usr/bin/python3

import requests, time

from layout.table import Table
from layout.layout import Layout

class Cookies:

    @classmethod
    def get_cookies(cls, url, filter_data = None):
        start_time = time.time()
        response = requests.get(url)
        
        Table.header([
            ("Name", "cyan", True),
            ("Value", "white", False)
        ])
        
        cookie_dict = response.cookies.get_dict()
        
        if filter_data:
            cookie_dict = {
                k: v for k, v in cookie_dict.items() if k.find(filter_data)
            }

        for name, value in cookie_dict.items():
            Table.row(name, value)

        end_time = "{:.2f}".format(time.time() - start_time)
        Table.caption(f"Total of cookies on page: {len(cookie_dict)} - Time taken: {end_time} seconds")
        Table.display()

    @classmethod
    def section(cls, url, filter_data):
        Layout.header_section("Cookies")
        cls.get_cookies(url, filter_data)
    