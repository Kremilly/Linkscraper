#!/usr/bin/python3

import os, base64
from urllib.parse import urlparse

from utils.url import URL

class File:
    
    @classmethod
    def open_read(cls, file, mode):
        f = open(file, 'r')
        return f.read()

    @classmethod
    def to_base64(cls, file):
        with open(file, 'rb') as f:
            output = base64.b64encode(f.read())
        
        return output

    @classmethod
    def get_file_name(cls, string):
        name = os.path.split(string)[1]

        if string.find('?'):
            return URL.remove_query(name)
        
        return name

    @classmethod
    def get_remote_file_name(cls, url):
        a = urlparse(url)
        basename = os.path.basename(a.path)
        
        if basename.find('.'):
            return basename
        
        for file in a.path.split('/'):
            if basename.find('.') and len(file) > 1:
                return file

    @classmethod
    def create_path(cls, folder):
        if os.path.isdir(folder) != True:
            os.makedirs(folder)

    @classmethod
    def open(cls, file):
        if os.path.exists(file):
            os.startfile(
                os.getcwd() + '\\' + file
            )
            
    @classmethod
    def write(cls, file_name, content, mode, enconding):
        with open(f'{file_name}', mode, encoding=enconding) as f:
            f.write(content)
