#!/usr/bin/python3

import os
from dotenv import load_dotenv

from helper.apis import Apis
from helper.configs import Configs

from utils.date_time import DateTime

class Env:
    
    file_name = '.env'
    
    @classmethod
    def write(cls, content):
        with open(cls.file_name, 'w') as f:
            f.write(f"# Env file created with {Configs.APP_NAME}\n"
                    f"# File generated in: {DateTime.get_datetime()}\n\n"
                    f"# Get key: {Apis.VIRUSTOTAL_API_KEY_URL}\nVIRUSTOTAL_KEY={content['virustotal']}\n\n"
                    f"# Get key: {Apis.IMGUR_API_KEY_URL}\nIMGUR_CLIENT_API={content['imgur']}\n\n"
                    f"# Get key: {Apis.GOOGLE_FONTS_API_KEY_URL}\nGOOGLE_FONTS_KEY={content['google_fonts']}\n")
    
    @classmethod    
    def get(cls, var_env):
        load_dotenv()
        return os.getenv(var_env)
