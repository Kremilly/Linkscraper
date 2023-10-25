#!/usr/bin/python3

import re
from classes.regex import Regex
from urllib.parse import urlparse, parse_qs

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
