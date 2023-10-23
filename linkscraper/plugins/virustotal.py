#!/usr/bin/python3

import requests, time
from utils.utils_http import *

from classes.env import Env

from layout.table import Table
from layout.layout import Layout

def plugin_virustotal(url):
    key = Env.get("VIRUSTOTAL_KEY")
    
    if not key:
        Layout.error("Key is required", False, True, {
            "text": "Get your VirusTotal key here:",
            "value": "https://www.virustotal.com/gui/my-apikey",
            "style": "bold green"
        })
    else:
        start_time = time.time()
        
        response = requests.post("https://www.virustotal.com/api/v3/urls", data="url=" + strip_scheme(url), headers={
            "x-apikey": key,
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        })
        
        if response.status_code != 200:
            if response.json()["error"]["code"] == "WrongCredentialsError":
                Layout.error("Key is invalid", False, True, {
                    "text": "Get your VirusTotal key here:",
                    "value": "https://www.virustotal.com/gui/my-apikey",
                    "style": "bold green"
                })
            else:
                Layout.error(response.json()['error']['message'], False, True)

        response = requests.get(response.json()["data"]["links"]["self"], headers={
            "x-apikey": key,
            "accept": "application/json",
        })

        resp_json = response.json()
        permalink = resp_json["data"]["links"]["item"].replace("api/v3/urls", "gui/url")

        Layout.print("\t\t", "Stats:")
        Layout.separator()

        Layout.print("[bold green]Harmless: [/bold green]", str(resp_json["data"]["attributes"]["stats"]["harmless"]))
        Layout.print("[bold red]Malicious: [/bold red]", str(resp_json["data"]["attributes"]["stats"]["malicious"]))
        Layout.print("[bold yellow]Suspicious: [/bold yellow]", str(resp_json["data"]["attributes"]["stats"]["suspicious"]))
        Layout.print("[bold cyan]Undetected: [/bold cyan]", str(resp_json["data"]["attributes"]["stats"]["undetected"]))

        Layout.separator()
        Layout.print("Permalink", permalink, "bold green")

        Layout.header_section("Result")
    
        Table.header([
            ("Engine", "cyan", True),
            ("Result", "white", False),
            ("Category", "white", False)
        ])

        for engine in resp_json["data"]["attributes"]["results"]:
            result = resp_json["data"]["attributes"]["results"][engine]["result"]
            category = resp_json["data"]["attributes"]["results"][engine]["category"]

            if result == "clean":
                Table.row(engine, f"[bold green]{result}[/bold green]")
            elif result == "unrated":
                Table.row(engine, f"[bold cyan]{result}[/bold cyan]")
            else:
                Table.row(engine, f"[bold red]{result}[/bold red]", f"[bold red]{category}[/bold red]")
                
        end_time = "{:.2f}".format(time.time() - start_time)
        
        Table.caption(f"Time taken: {end_time} seconds")
        Table.display()
