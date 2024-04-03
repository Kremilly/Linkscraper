#!/usr/bin/python3

import whois, time

from utils.http import HTTP
from utils.date_time import DateTime

from layout.table import Table

class Whois:

    @classmethod
    def run(cls, url):
        start_time = time.time()
        domain_name = HTTP.get_hostname(url)
        whois_info = whois.whois(domain_name)

        Table.header([
            ('Name', 'cyan', True),
            ('Value', 'white', False)
        ])

        Table.row('Domain name', f'{whois_info.domain_name}')
        Table.row('Domain registrar', f'{whois_info.registrar}')
        Table.row('WHOIS server', f'{whois_info.whois_server}')
        Table.row('Domain creation date', f'{str(whois_info.creation_date)}')
        Table.row('Expiration date', f'{str(whois_info.expiration_date)}')
        
        Table.caption(f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        Table.display()
