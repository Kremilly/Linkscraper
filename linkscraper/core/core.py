#!/usr/bin/python3

import time
from datetime import datetime

from utils.http import HTTP

from layout.layout import Layout

class Core:
    
    @classmethod
    def today_datetime(cls):
        today = datetime.today()
        return today.strftime("%a, %b %d %Y - %I:%M:%S %p")

    @classmethod
    def basic(cls, url):
        Layout.header_section("Core")    
        start_time = time.time()
        
        Layout.print("IP Address:", HTTP.get_ip(url))
        Layout.print("HTTP Code:", HTTP.code(url))
        Layout.print("HTTP Code Message:", HTTP.code_list(HTTP.code(url)))

        if HTTP.check_https_url(url):
            Layout.print("HTTPS Status:", "Secure", "bold green")
        elif HTTP.check_http_url(url):
            Layout.print("HTTPS Status", "Not secure", "bold red")
        
        Layout.time_taken(start_time, True)

    @classmethod
    def home(cls, url):
        Layout.print("Target:", url, "bold green")
        Layout.print("Hostname:", HTTP.get_hostname(url), "bold blue")
        Layout.print("Scan:", cls.today_datetime(), "italic cyan")
