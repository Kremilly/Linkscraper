#!/usr/bin/python3

import requests

from http import HTTPStatus

from helper.apis import Apis

from utils.http import HTTP

from layout.layout import Layout

class VirusTotal:
    
    @classmethod
    def stats(cls, params):
        Layout.print("\t\t", "Stats:")
        Layout.separator()
        
        Layout.print("[bold green]Harmless[/bold green]:", str(params["harmless"]))
        Layout.print("[bold red]Malicious[/bold red]:", str(params["malicious"]))
        Layout.print("[bold yellow]Suspicious[/bold yellow]:", str(params["suspicious"]))
        Layout.print("[bold cyan]Undetected[/bold cyan]:", str(params["undetected"]))
    
    @classmethod
    def error(cls, message, additional_print = True):
        if additional_print:
            return Layout.error(message, False, True, {
                "style": "bold blue",
                "text": "Get your VirusTotal key here:",
                "value": Apis.VIRUSTOTAL_API_KEY_URL.value,
            })
            
        return Layout.error(message, False, True)
        
    @classmethod
    def request(cls, url, key):
        response = requests.post(Apis.VIRUSTOTAL_API_REQUEST.value, data="url=" + HTTP.strip_scheme(url), headers={
            "x-apikey": key,
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        })
        
        if not response.status_code is HTTPStatus.OK:
            if response.json()["error"]["code"] == "WrongCredentialsError":
                cls.error("Key is invalid")
                
            cls.error(response.json()['error']['message'], False)

        response = requests.get(response.json()["data"]["links"]["self"], headers={
            "x-apikey": key,
            "accept": "application/json",
        })

        return response.json()
