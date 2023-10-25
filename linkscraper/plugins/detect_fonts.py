#!/usr/bin/python3

import requests, time, re
from bs4 import BeautifulSoup

from rich.prompt import Prompt
from layout.table import Table
from apis.google_fonts import GoogleFonts

def get_css_links(url):
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

def get_fonts_from_css_files(url):
    css_links = get_css_links(url)  # Presumindo que esta função já esteja definida em algum lugar do seu código
    font_families = []

    for link in css_links:
        response = requests.get(link)
        css_content = response.text

        matches = re.findall(
            r'font-family\s*:\s*([^;}]+)', css_content
        )
        
        for match in matches:
            fonts = [
                f.strip().replace(
                    '"', ''
                ).replace(
                    "'", ""
                ).replace(
                    ")", ""
                ).replace(
                    "var(", ""
                ).replace(
                    "!important", ""
                ) for f in match.split(',')
            ]
            
            fonts = [
                f for f in fonts if f not in [
                    "important", "inherit", "var"
                ]
            ]
            
            font_families.extend(fonts)
    
    return list(
        set(font_families)
    )

def get_fonts_from_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    fonts = ''

    body_style = soup.find('body').attrs.get('style', '')
    if 'font-family' in body_style:
        fonts = body_style.split('font-family:')[1].split(';')[0].strip().split('}')[0].replace('"', '')
        
    for style_tag in soup.find_all('style'):
        if 'font-family' in style_tag.string:
            fonts = style_tag.string.split('font-family:')[1].split(';')[0].strip().split('}')[0].replace('"', '')
            
    list_fonts = fonts.split(',')
    
    return list(
        set(list_fonts)
    )

def plugin_detect_fonts(url, google_fonts = None, download = None):
    start_time = time.time()
    font_families = get_fonts_from_css_files(url)
    
    if len(font_families) == 0:
        font_families = get_fonts_from_html(url)
        
    if google_fonts is not None:
        font_name = Prompt.ask(f"Enter the font name", choices=font_families)
        GoogleFonts.list(url, font_name, download)
    else:
        Table.header([
            ("Name", "cyan", True),
            ("Value", "white", False)
        ])
        
        for font_name in font_families:
            Table.row("font-family", font_name.strip())

        end_time = "{:.2f}".format(time.time() - start_time)
        
        if google_fonts is not None:
            font_name = Prompt.ask(f"Enter the font name", choices=font_families)
            GoogleFonts.list(url, font_name, download)
        
        Table.caption(f"Total of fonts: {len(font_families)} - Time taken: {end_time} seconds")
        Table.display()
