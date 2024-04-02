#!/usr/bin/python3

import time, requests

from layout.layout import Layout

class Robots:

    @classmethod
    def run(cls, url):
        start_time = time.time()
        robots_url = url + '/robots.txt'
        
        try:
            response = requests.get(robots_url)
            response.raise_for_status()
            robots = response.text

            for line in robots.split('\n'):
                match (line):
                    case _ if 'Allow' in line:
                        Layout.print(None, line, 'green')
                    case _ if 'Disallow' in line:
                        Layout.print(None, line, 'red')
                    case _ if 'Sitemap' in line:
                        Layout.print(None, line, 'italic cyan')
                    case _ if 'User-agent' in line:
                        Layout.print(None, line, 'italic yellow')
                    case _:
                        Layout.print(None, line, 'white')
        
            Layout.time_taken(start_time, True)
        except requests.RequestException as e:
            Layout.error(e, False, True)
