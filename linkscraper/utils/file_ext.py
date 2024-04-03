#!/usr/bin/python3

import os

from helper.configs import Configs

class FileExt:
    
    @classmethod
    def remove(cls, file):
        return file.rsplit(".", 1)[0]
    
    @classmethod
    def is_valid(cls, file):
        _, extension = os.path.splitext(file)
        return extension.lower() in Configs.ALLOWED_EXT.value

    @classmethod
    def get(cls, file):
        ext = os.path.splitext(file)
        
        if ext != "" or ext != ".":
            return ext
        
        return None
