#!/usr/bin/python3
import socket, requests, urllib

from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

from helper.configs import Configs

class HTTP:
    
    @classmethod  
    def strip_scheme(cls, url):
        parsed = urlparse(url)
        
        return parsed.geturl().replace(
            "%s://" % parsed.scheme, '', 1
        )
 
    @classmethod    
    def code_list(cls, c):
        r = requests.get(Configs.LIST_HTTP_STATUS.value)
        r = r.json()

        for code in r:
            if code == str(c):
                return "[italic yellow][link=" + r[code]["spec_href"] + "]" + r[code]["message"] + "[/link][/italic yellow]"

    @classmethod  
    def code(cls, url):
        try:
            return str(
                requests.head(url).status_code
            )
        
        except requests.ConnectionError:
            return False

    @classmethod  
    def get_ip(cls, url):
        url = cls.strip_scheme(url)
        return socket.gethostbyname(url)

    @classmethod
    def get_hostname(cls, url):
        return urlparse(url).netloc
    
    @classmethod
    def check_protocol_url(cls, url, https = False):
        link = f'http://{url}'
        
        protocol_url = urlparse(link)
        connection = HTTPConnection(protocol_url.netloc)
        
        if https:
            link = link.replace('http', 'https')
            connection = HTTPSConnection(protocol_url.netloc)
        
        try:
            connection.request('HEAD', protocol_url.path)
            
            if connection.getresponse():
                return True
            
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
