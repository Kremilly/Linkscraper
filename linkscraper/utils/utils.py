#!/usr/bin/python3

import urllib.request
import re, requests, json

from decouple import config
from urllib.parse import urlparse

from utils.configs import *

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
    url_pattern_check_protocol = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    
    if string == None:
        return False
    else:
        if check_protocol == True:
            if re.match(url_pattern_check_protocol, string) != None:
                return True
            else:
                return False
        elif check_protocol == False:
            if re.match(url_pattern, string) != None:
                return True
            else:
                return False

def get_env(string):
    if find(string, "env:") or find(string, "ENV:"):
        return config(string.split(":")[1])
    else:
        return string

def check_connection(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
