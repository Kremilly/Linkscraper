#!/usr/bin/python3

from classes.configs import Configs

import socket, requests, urllib
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

class HTTP:
    
    @classmethod  
    def strip_scheme(cls, url):
        parsed = urlparse(url)
        scheme = "%s://" % parsed.scheme
        
        return parsed.geturl().replace(
            scheme, '', 1
        )
 
    @classmethod    
    def code_list(cls, c):
        r = requests.get(Configs.LIST_HTTP_STATUS.value)
        r = r.json()

        for code in r:
            if code == str(c):
                return "[italic yellow]" + r[code]["message"] + " [/italic yellow]-> [bold green]" + r[code]["spec_href"] + "[/bold green]"

    @classmethod  
    def code(cls, url):
        try:
            r = requests.head(url)
            return str(r.status_code)
        except requests.ConnectionError:
            return False

    @classmethod  
    def get_ip(cls, url):
        url = cls.strip_scheme(url)
        return socket.gethostbyname(url)

    @classmethod  
    def get_hostname(cls, url):
        parsed = urlparse(url)
        return parsed.netloc

    @classmethod  
    def check_https_url(cls, url):
        url = cls.strip_scheme(url)
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

    @classmethod  
    def check_http_url(cls, url):
        url = cls.strip_scheme(url)
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
        
    @classmethod 
    def check_connection(cls, host):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False
