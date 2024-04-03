#!/usr/bin/python3

import requests, cloudscraper, time

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from utils.locale import Locale

from helper.configs import Configs

from layout.table import Table
from layout.layout import Layout

class PageDetails:

    @classmethod
    def language_country(cls, code, param):
        if param == 'locale':
            return f'{Locale.language(code)} ({Locale.country(code)})'
        
        return False

    @classmethod
    def wp_detect(cls, url):
        session = requests.Session()
        session.headers['User-Agent'] = Configs.DEFAULT_USER_AGENT.value
        
        soup = BeautifulSoup(session.get(url).content, 'html.parser')
        metas = soup.find_all('meta')
        
        wp_detected = False
        
        wp_meta_generator = [ 
            meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'generator' 
        ]

        if len(wp_meta_generator) >= 1 and wp_meta_generator[0].find('WordPress'):
            wp_detected = True
            wp_version = wp_meta_generator[0]
            
        for css in soup.find_all('link'):
            if css.attrs.get('href'):
                css_url = urljoin(url, css.attrs.get('href'))

                if css_url.find('wp-content') or css_url.find('wp-includes'):
                    wp_detected = True
                    
                wp_detected = False
                
                break

        if wp_detected:
            Layout.print(f'[blue]WordPress[/blue]:', 'detected', 'green')
            Layout.print(f'[blue]WordPress version[/blue]:', wp_version, 'green')
            
        Layout.print(f'[blue]WordPress[/blue]:', 'not detected', 'red')

    @classmethod
    def run(cls, url):
        start_time = time.time()
        scraper = cloudscraper.create_scraper() 
        
        html = scraper.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
            
        metatitle = (soup.find('title')).get_text()
        metadescription = soup.find('meta',attrs={'name':'description'})
        robots_directives = soup.find('meta',attrs={'name':'robots'})
        viewport = soup.find('meta',attrs={'name':'viewport'})
        charset = soup.find('meta',attrs={'charset':True})
        open_graph = [[a['property'].replace('og:',''),a['content']] for a in soup.select('meta[property^=og]')]

        Layout.print('[blue]Title:[/blue]', metatitle)
        if metadescription: Layout.print('[blue]Description:[/blue]', metadescription['content'])
        if robots_directives: Layout.print('[blue]Robots directives:[/blue]', robots_directives['content'].split(','))
        if viewport: Layout.print('[blue]Viewport:[/blue]', viewport['content'])
        if charset: Layout.print('[blue]Charset:[/blue]', charset['charset'])
        
        cls.wp_detect(url)

        if open_graph:
            Layout.separator()
            Layout.print(f'[blue]What is Open Graph?[/blue]', 'The Open Graph protocol enables any web page to become a rich object in a social graph. For instance, this is used on Facebook to allow any web page to have the same functionality as any other object on Facebook.')
            Layout.print(f'[blue]Documentation[/blue]:', 'https://ogp.me', 'bold blue')
            Layout.separator()
        
            Table.header([
                ('Name', 'cyan', True),
                ('Value', 'white', False)
            ])

            for info in open_graph:
                if not cls.language_country(info[1], info[0]):
                    Table.row('og:' + info[0], info[1])
                else:
                    Table.row('og:' + info[0], cls.language_country(info[1], info[0]))    
            
            Table.display()
        
        Layout.time_taken(start_time, True)
