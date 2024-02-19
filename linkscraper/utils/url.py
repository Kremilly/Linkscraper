#!/usr/bin/python3

import re
from classes.regex import Regex
from urllib.parse import urlparse, parse_qs

from utils.http import HTTP

from layout.layout import Layout

class URL:
    
    @classmethod
    def remove_query(cls, url):
        split = url.split("?")[1]
        return url.replace("?" + split, "")
    
    @classmethod
    def extract_query_params(cls, url):
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)
        
    @classmethod
    def is_url(cls, url, check_protocol = True):
        if url == None:
            return False
        else:
            if check_protocol == True:
                if re.match(Regex.URL_PATTERN_CHECK_PROTOCOL.value, url) != None:
                    return True
                else:
                    return False
            elif check_protocol == False:
                if re.match(Regex.URL_PATTERN_PROTOCOL.value, url) != None:
                    return True
                else:
                    return False
    
    @classmethod
    def check_url_and_connection(cls, url):
        if not cls.is_url(url):
            Layout.error("URL is missing", False, True)
            
        if not HTTP.check_connection(url):
            Layout.error("connection is not established", False, True)
