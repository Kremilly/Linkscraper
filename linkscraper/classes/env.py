#!/usr/bin/python3

from decouple import config
from classes.configs import Configs

class Env:
    
    file_name = '.env'
    
    @classmethod  
    def open_file(cls, mode):
        return open(cls.file_name, mode)
    
    @classmethod   
    def read(cls):
        f = cls.open_file("r")
        return f.read()
    
    @classmethod   
    def write(cls, content, mode = 'w'):
        f = cls.open_file(mode)
        f.write(f"# Env file created with {Configs.APP_NAME.value} (v.{Configs.VERSION.value})\n\n# Get key: {Configs.VIRUSTOTAL_API_KEY_URL.value}\nVIRUSTOTAL_KEY={content['virustotal']}\n\n# Get key: {Configs.IMGUR_API_KEY_URL.value}\nIMGUR_CLIENT_API={content['imgur']}\n")
        f.close()
    
    @classmethod    
    def get(cls, var_env):
        var = config(var_env)
        
        if var: return var 
        return None
