#!/usr/bin/python3

from classes.env import Env
from classes.configs import *

from plugins.autoload import *
from layout.layout import Layout

from rich.prompt import Prompt

def write_env():
    imgur_key_url = Configs.IMGUR_API_KEY_URL.value
    virustotal_key_url = Configs.VIRUSTOTAL_API_KEY_URL.value
    
    virustotal_key = Prompt.ask(f"Enter your VirusTotal API key (get [blue bold][link={virustotal_key_url}]here[/link][/blue bold])")
    imgur_key = Prompt.ask(f"Enter your Imgur Client ID (get [blue bold][link={imgur_key_url}]here[/link][/blue bold])")
    
    if not virustotal_key == '' and not imgur_key == '':
        Env.write({
            "imgur": imgur_key,
            "virustotal": virustotal_key,
        })
        
    Layout.success("Env file written successfully.", True)
