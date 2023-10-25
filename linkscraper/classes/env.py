#!/usr/bin/python3

from decouple import config
from datetime import datetime

from apis.apis import Apis
from classes.configs import Configs

class Env:
    
    file_name = '.env'
    
    @classmethod  
    def open_file(cls, mode):
        return open(cls.file_name, mode)
    
    @classmethod
    def get_datetime(cls):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')
    
    @classmethod   
    def read(cls):
        f = cls.open_file("r")
        return f.read()
    
    @classmethod   
    def write(cls, content, mode = 'w'):
        f = cls.open_file(mode)
        f.write(f"# Env file created with {Configs.APP_NAME.value} (v.{Configs.VERSION.value})\n# File generated in: {cls.get_datetime()}\n\n# Get key: {Apis.VIRUSTOTAL_API_KEY_URL.value}\nVIRUSTOTAL_KEY={content['virustotal']}\n\n# Get key: {Apis.IMGUR_API_KEY_URL.value}\nIMGUR_CLIENT_API={content['imgur']}\n\n# Get key: {Apis.GOOGLE_FONTS_API_KEY_URL.value}\nGOOGLE_FONTS_KEY={content['google_fonts']}\n")
        f.close()
    
    @classmethod    
    def get(cls, var_env):
        var = config(var_env)
        
        if var: return var 
        return None
