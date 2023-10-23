#!/usr/bin/python3

import random as r
import urllib.request
import re, requests, json

from urllib.parse import urlparse

from classes.regex import Regex
from classes.configs import Configs

def remove_query(url):
    split = url.split("?")[1]
    return url.replace("?" + split, "")

def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes>>10, units[1:])

def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)

def country(country):
    if find(country, "_"):
        country = country.split("_")[1].lower()
    else:
        country = country.lower()

    if not country:
        country = country

    r = requests.get(Configs.LIST_COUNTRYS.value)
    r = r.json()

    for code in r:
        if code['alpha2'] == country:
            return code['name']

def language(lang):
    if find(lang, "_"):
        lang = lang.split("_")[0].lower()
    else:
        lang = lang.lower()

    r = requests.get(Configs.LIST_LANGUAGES.value)
    r = r.json()

    for code in r:
        if code['code'] == lang:
            return code['name']

def find(string, find):
    if string.find(find) != -1:
        return True
    else:
        return False

def is_json(string):
    try:
        if json.loads(string):
            return True
        else:
            return False
    except ValueError as e:
        return False

def is_url(string, check_protocol = True):
    if string == None:
        return False
    else:
        if check_protocol == True:
            if re.match(Regex.URL_PATTERN_CHECK_PROTOCOL.value, string) != None:
                return True
            else:
                return False
        elif check_protocol == False:
            if re.match(Regex.URL_PATTERN_PROTOCOL.value, string) != None:
                return True
            else:
                return False

def check_connection(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def generate_id():
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for _ in range(0, 10):
        random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
        
    return random_string
