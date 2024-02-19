#!/usr/bin/python3

from apis.apis import Apis
from classes.env import Env

from layout.layout import Layout

from rich.prompt import Prompt

class WriteEnv:

    @classmethod
    def run():
        imgur_key_url = Apis.IMGUR_API_KEY_URL.value
        virustotal_key_url = Apis.VIRUSTOTAL_API_KEY_URL.value
        google_fonts_key_url = Apis.GOOGLE_FONTS_API_KEY_URL.value
        
        imgur_key = Prompt.ask(f"Enter your Imgur Client ID (get [blue bold][link={imgur_key_url}]here[/link][/blue bold])")
        virustotal_key = Prompt.ask(f"Enter your VirusTotal API key (get [blue bold][link={virustotal_key_url}]here[/link][/blue bold])")
        google_fonts_key = Prompt.ask(f"Enter your Google Fonts API Key (get [blue bold][link={google_fonts_key_url}]here[/link][/blue bold])")
        
        Env.write({
            "imgur": imgur_key,
            "virustotal": virustotal_key,
            "google_fonts": google_fonts_key,
        })
            
        Layout.success("Env file written successfully.", True)
