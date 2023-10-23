#!/usr/bin/python3

import time
from datetime import datetime

from core.headers import *
from core.scraper import *
from core.cookies import *

from layout.layout import *

from classes.configs import *
from utils.utils_http import *

from core.static.js import *
from core.static.css import *
from core.static.images import *

from plugins.autoload import *

def run_core(url):
    Layout.header_section("Core")    
    start_time = time.time()
    
    Layout.print("IP Address:", get_ip(url))
    Layout.print("HTTP Code:", str(http_code(url)))
    Layout.print("HTTP Code Message:", http_code_list(http_code(url)))

    if check_https_url(url):
        Layout.print("HTTPS Status:", "Secure", "bold green")
    elif check_http_url(url):
        Layout.print("HTTPS Status", "Not secure", "bold red")
    
    Layout.time_taken(start_time)

def run_headers(url, filter_data):
    Layout.header_section("Headers")
    get_headers(url, filter_data)

def run_cookies(url, filter_data):
    Layout.header_section("Cookies")
    get_cookies(url, filter_data)

def run_get_js_files(url, minify_files, filter_data, download):
    Layout.header_section("Scripts JavaScript")
    js_files(url, minify_files, filter_data, download)

def run_get_css_files(url, minify_files, filter_data, download):
    Layout.header_section("CSS Files")
    css_files(url, minify_files, filter_data, download)

def run_get_images_files(url, filter_data, download):
    Layout.header_section("Images")
    images_files(url, filter_data, download)

def run_get_links(url, external_links, status_code, filter_data):
    Layout.header_section("Links")
    get_links(url, external_links, status_code, filter_data)

def run_get_emails(url, filter_data):
    Layout.header_section("Emails")
    get_emails(url, filter_data)

def run_home(url):
    today = datetime.today()
    datetime_obj = today.strftime("%a, %b %d %Y - %I:%M:%S %p")
    
    Layout.print("Target:", url, "bold green")
    Layout.print("Hostname:", get_hostname(url), "bold blue")
    Layout.print("Scan:", datetime_obj, "italic cyan")

def run_plugin(plugin, url, browser=None, upload=None, title=None):
    Layout.header_plugin(plugin)

    if plugin == "whois":
        plugin_whois(url)
    elif plugin == "robots":
        plugin_robots(url)
    elif plugin == "page-details":
        plugin_page_details(url)
    elif plugin == "virustotal":
        plugin_virustotal(url)
    elif plugin == "ip-location":
        plugin_ip_location(url)
    elif plugin == "screenshot":
        plugin_screenshot(url, browser, upload, title)
    elif plugin == "detect-fonts":
        plugin_detect_fonts(url)
    elif plugin == "extract-colors":
        plugin_extract_colors(url)
    else:
        Layout.error("Plugin invalid", False, True)

def check_url_and_connection(url):
    if not is_url(url):
        Layout.error("URL is missing", False, True)
        
    if not check_connection(url):
        Layout.error("connection is not established", False, True)
