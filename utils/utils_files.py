#!/usr/bin/python3

import os, requests, base64
from urllib.parse import urlparse

from utils.utils import *

def local_file_size(file):
    file_size = os.stat(file)
    return humanSize(file_size.st_size)

def remote_file_size(url):
    try:
        req_headers = requests.get(url)
        return humanSize(
            int(req_headers.headers["Content-Length"])
        )
    except:
        return None

def to_base64(file):
    with open(file, "rb") as f:
        output = base64.b64encode(f.read())
    
    return output

def remove_extension(file):
    return file.rsplit(".", 1)[0]

def get_extension(file):
    ext = os.path.splitext(file)
    
    if ext != "" or ext != ".":
        return ext
    else:
        return None

def get_file_name(string):
    name = os.path.split(string)[1]
        
    if find(string, "?"):
        return removeQuery(name)
    else:
        return name

def get_remote_file_size(url):
    a = urlparse(url)
    basename = os.path.basename(a.path)
    
    if find(basename, "."):
        return basename
    else:
        for file in a.path.split("/"):
            if find(file, ".") and len(file) > 1:
                return file

def create_folder(folder):
    if os.path.isdir(folder) != True:
        os.makedirs(folder)
