#!/usr/bin/python3

from utils.utils import *
from classes.configs import *

import socket, requests
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

def http_code_list(c):
    r = requests.get(Configs.LIST_HTTP_STATUS.value)
    r = r.json()

    for code in r:
        if code == str(c):
            return "[italic yellow]" + r[code]["message"] + " [/italic yellow]-> [bold green]" + r[code]["spec_href"] + "[/bold green]"

def http_code(url):
    try:
        r = requests.head(url)
        return r.status_code
    except requests.ConnectionError:
        return False

def get_ip(url):
    url = strip_scheme(url)
    return socket.gethostbyname(url)

def get_hostname(url):
    parsed = urlparse(url)
    return parsed.netloc

def check_https_url(url):
    url = strip_scheme(url)
    https_url = f'https://{url}'

    try:
        https_url = urlparse(https_url)
        connection = HTTPSConnection(https_url.netloc, timeout=2)
        connection.request('HEAD', https_url.path)
        
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False

def check_http_url(url):
    url = strip_scheme(url)
    http_url = f'http://{url}'

    try:
        http_url = urlparse(http_url)
        connection = HTTPConnection(http_url.netloc)
        connection.request('HEAD', http_url.path)
        
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False
