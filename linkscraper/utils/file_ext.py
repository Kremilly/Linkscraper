#!/usr/bin/python3

import os, requests

from classes.settings import Settings

class FileExt:
    
    @classmethod
    def remove(cls, file):
        return file.rsplit('.', 1)[0]
    
    @classmethod
    def is_valid(cls, file):
        _, extension = os.path.splitext(file)
        dataset_allowed_ext = Settings.get('dataset.list_allowed_extensions', 'STRING')
        
        ext = requests.get(dataset_allowed_ext).json()        
        all_ext = ext['scripts'] + ext['styles'] + ext['images']
        
        return extension.lower() in all_ext

    @classmethod
    def get(cls, file):
        ext = os.path.splitext(file)
        
        if ext != '' or ext != '.':
            return ext
        
        return None
