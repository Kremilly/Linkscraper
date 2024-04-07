import sys, requests, time
from concurrent.futures import ThreadPoolExecutor

from rich.progress import Progress

from utils.http import HTTP
from utils.date_time import DateTime

from helper.apis import Apis

from layout.table import Table

class Subdomains:
    
    @classmethod
    def get_status(cls, item, protocol):
        url = protocol + item
        http_code = HTTP.code(url)
        http_reason = HTTP.code_list(http_code)
        
        if http_code == False:
            http_reason = 'Offline'
        
        Table.row(item, str(http_code), http_reason, url)

    @classmethod
    def run(cls, url):
        start_time = time.time()
        
        domain = HTTP.strip_scheme(url)
        protocol = HTTP.get_scheme(url) + '://'
        
        resp_json = requests.get(Apis.THREATCROWD_API_REQUEST, params={
            'domain': domain
        }).json()
        
        total_subdomains = len(resp_json['subdomains'])
        
        Table.header([
            ('Subdomain', 'cyan', True),
            ('Status code', 'white', False),
            ('HTTP message', 'yellow', False),
            ('Link', 'bold blue', False)
        ])
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Fetching subdomains...", total=total_subdomains)

            with ThreadPoolExecutor(max_workers=5) as executor:
                for _ in executor.map(lambda item: cls.get_status(item, protocol), resp_json['subdomains']):
                    progress.advance(task)

        Table.caption(f'Total of subdomains: {total_subdomains} - '
                      f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        
        Table.display()
