#!/usr/bin/python3

import sys, time
from urllib.request import urlopen

from utils.http import HTTP
from layout.layout import Layout

def plugin_robots(url):
    start_time = time.time()
    
    robots_url = url + "/robots.txt"
    status_code = HTTP.code(robots_url)
    
    if status_code == 404:
        Layout.error("robots.txt not exists", False, True)
    else:
        with urlopen(robots_url) as stream:
            robots = stream.read().decode("utf-8")

            for line in robots.split("\n"):
                if line.find("Allow") != -1:
                    Layout.print(None, line, "green")
                elif line.find("Disallow") != -1:
                    Layout.print(None, line, "red")
                elif line.find("Sitemap") != -1:
                    Layout.print(None, line, "italic cyan")
                elif line.find("User-agent") != -1:
                    Layout.print(None, line, "italic yellow")
                else:
                    Layout.print(None, line, "white")
    
    Layout.time_taken(start_time, True)
