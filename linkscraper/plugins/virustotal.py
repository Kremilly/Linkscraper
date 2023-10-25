#!/usr/bin/python3

import time

from classes.env import Env

from apis.virustotal import VirusTotal

from layout.table import Table
from layout.layout import Layout

def plugin_virustotal(url):
    key = Env.get("VIRUSTOTAL_KEY")
    
    if not key:
        VirusTotal.error("Key is requiired")
    else:
        start_time = time.time()
        resp_json = VirusTotal.request(url, key)
        permalink = resp_json["data"]["links"]["item"].replace("api/v3/urls", "gui/url")

        VirusTotal.stats({
            "harmless": resp_json["data"]["attributes"]["stats"]["harmless"],
            "malicious": resp_json["data"]["attributes"]["stats"]["malicious"],
            "suspicious": resp_json["data"]["attributes"]["stats"]["suspicious"],
            "undetected": resp_json["data"]["attributes"]["stats"]["undetected"],
        })

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
