#!/usr/bin/python3

from decouple import config

from apis.apis import Apis
from classes.configs import Configs

from utils.file import File
from utils.date_time import DateTime

class Env:
    
    file_name = '.env'
    
    @classmethod   
    def write(cls, content, mode = 'w'):
        f = File.open_read(cls.file_name, mode)
        
        f.write(f"# Env file created with {Configs.APP_NAME.value} (v.{Configs.VERSION.value})\n"
                f"# File generated in: {DateTime.get_datetime()}\n\n"
                f"# Get key: {Apis.VIRUSTOTAL_API_KEY_URL.value}\nVIRUSTOTAL_KEY={content['virustotal']}\n\n"
                f"# Get key: {Apis.IMGUR_API_KEY_URL.value}\nIMGUR_CLIENT_API={content['imgur']}\n\n"
                f"# Get key: {Apis.GOOGLE_FONTS_API_KEY_URL.value}\nGOOGLE_FONTS_KEY={content['google_fonts']}\n")
        
        f.close()
    
    @classmethod    
    def get(cls, var_env):
        var = config(var_env)
        
        if var:
            return var
        
        return None
