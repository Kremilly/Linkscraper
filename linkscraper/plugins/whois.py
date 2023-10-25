#!/usr/bin/python3

import whois, time

from utils.http import HTTP
from layout.table import Table

def plugin_whois(url):
    start_time = time.time()
    domain_name = HTTP.get_hostname(url)
    whois_info = whois.whois(domain_name)

    Table.header([
        ("Name", "cyan", True),
        ("Value", "white", False)
    ])

    Table.row("Domain name", f"{whois_info.domain_name}")
    Table.row("Domain registrar", f"{whois_info.registrar}")
    Table.row("WHOIS server", f"{whois_info.whois_server}")
    Table.row("Domain creation date", f"{str(whois_info.creation_date)}")
    Table.row("Expiration date", f"{str(whois_info.expiration_date)}")
    
    end_time = "{:.2f}".format(time.time() - start_time)
    Table.caption(f"Time taken: {end_time} seconds")
    Table.display()
