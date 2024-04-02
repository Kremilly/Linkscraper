#!/usr/bin/python3

import requests, time, re
from bs4 import BeautifulSoup

from rich.prompt import Prompt
from layout.table import Table
from apis.google_fonts import GoogleFonts

class DetectFonts:
    
    @classmethod
    def process_font_string(cls, font_str):
        replacements = [''', ''', ')', 'var(', '!important']
        
        for replacement in replacements:
            font_str = font_str.replace(replacement, '')
            
        return font_str.strip()
    
    @classmethod
    def get_css_links(cls, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        css_links = []
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            
            if href:
                if 'http' not in href:
                    href = requests.compat.urljoin(url, href)
                    
                css_links.append(href)
        
        return css_links
    
    @classmethod
    def get_fonts_from_css_files(cls, url):
        css_links = cls.get_css_links(url)
        font_families = []

        for link in css_links:
            response = requests.get(link)
            css_content = response.text

            matches = re.findall(
                r'font-family\s*:\s*([^;}]+)', css_content
            )
            
            for match in matches:
                fonts = [cls.process_font_string(f) for f in match.split(',')]
                
                fonts = [
                    f for f in fonts if f not in [
                        'important', 'inherit', 'var'
                    ]
                ]
                
                font_families.extend(fonts)
        
        return list(
            set(font_families)
        )

    @classmethod
    def get_fonts_from_html(cls, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        fonts = ''

        body_style = soup.find('body').attrs.get('style', '')
        if 'font-family' in body_style:
            fonts = body_style.split('font-family:')[1].split(';')[0].strip().split('}')[0].replace(''', '')
            
        for style_tag in soup.find_all('style'):
            if 'font-family' in style_tag.string:
                fonts = style_tag.string.split('font-family:')[1].split(';')[0].strip().split('}')[0].replace(''', '')
                
        list_fonts = fonts.split(',')
        
        return list(
            set(list_fonts)
        )
        
    @classmethod
    def run(cls, url, google_fonts = None, download = None) -> GoogleFonts|Table:
        start_time = time.time()
        font_families = cls.get_fonts_from_css_files(url)
        
        if len(font_families) == 0:
            font_families = cls.get_fonts_from_html(url)
            
        if google_fonts is None:
            font_name = Prompt.ask(f'Enter the font name', choices=font_families)
            return GoogleFonts.list(url, font_name, download)
        
        Table.header([
            ('Name', 'cyan', True),
            ('Value', 'white', False)
        ])
        
        for font_name in font_families:
            Table.row('font-family', font_name.strip())

        end_time = '{:.2f}'.format(time.time() - start_time)
        
        Table.caption(f'Total of fonts: {len(font_families)} - Time taken: {end_time} seconds')
        return Table.display()
