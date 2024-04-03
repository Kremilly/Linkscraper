#!/usr/bin/python3

import time

from utils.http import HTTP
from utils.date_time import DateTime

from layout.layout import Layout

from plugins.ip_location import IPLocation

class Core:

    @classmethod
    def basic(cls, url):
        start_time = time.time()
        Layout.header_section("Core")    
        
        Layout.print("IP Address:", HTTP.get_ip(url))
        Layout.print("HTTP Code:", HTTP.code(url))
        Layout.print("HTTP Code Message:", HTTP.code_list(HTTP.code(url)))

        if HTTP.check_protocol_url(url, True):
            Layout.print("HTTPS Status:", "Secure", "bold green")
        elif HTTP.check_protocol_url(url):
            Layout.print("HTTPS Status", "Not secure", "bold red")
        
        Layout.time_taken(start_time, True)

    @classmethod
    def home(cls, url):
        location = f"{IPLocation.ip_data('city')}, {IPLocation.ip_data('regionName')} - {IPLocation.ip_data('country')}"
                                                                                    
        Layout.print("Public IP:", IPLocation.ip_data('query'), "italic white")
        Layout.print("ISP:", IPLocation.ip_data('isp'), "italic cyan")
        Layout.print("Location:", f"{ location }", "italic green")
        Layout.separator()
        
        Layout.print("Target:", url, "bold green")
        Layout.print("Hostname:", HTTP.get_hostname(url), "bold blue")
        Layout.print("Scan:", DateTime.today_datetime(), "italic cyan")
