#!/usr/bin/python3

from apis.apis import Apis
from classes.env import Env

from rich.prompt import Prompt
from layout.layout import Layout

class WriteEnv:

    @classmethod
    def run(cls):
        imgur_key = Prompt.ask(f"Enter your Imgur Client ID (get [blue bold][link={Apis.IMGUR_API_KEY_URL.value}]here[/link][/blue bold])")
        virustotal_key = Prompt.ask(f"Enter your VirusTotal API key (get [blue bold][link={Apis.VIRUSTOTAL_API_KEY_URL.value}]here[/link][/blue bold])")
        google_fonts_key = Prompt.ask(f"Enter your Google Fonts API Key (get [blue bold][link={Apis.GOOGLE_FONTS_API_KEY_URL.value}]here[/link][/blue bold])")
        
        Env.write({
            "imgur": imgur_key,
            "virustotal": virustotal_key,
            "google_fonts": google_fonts_key,
        })
        
        Layout.success("Env file written successfully.", True)
