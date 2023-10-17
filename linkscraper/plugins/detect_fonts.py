#!/usr/bin/python3

import requests, time
from bs4 import BeautifulSoup

from rich.table import Table
from rich.console import Console

console = Console(record=True)

def plugin_detect_font(url):
    start_time = time.time()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    fonts = ''

    body_style = soup.find('body').attrs.get('style', '')
    if 'font-family' in body_style:
        fonts = body_style.split('font-family:')[1].split(';')[0].strip().split('}')[0]

    for style_tag in soup.find_all('style'):
        if 'font-family' in style_tag.string:
            fonts = style_tag.string.split('font-family:')[1].split(';')[0].strip().split('}')[0]
            
    end_time = "{:.2f}".format(time.time() - start_time)
    
    if fonts == '':
        console.print(f"[bold red]Fonts not detected[/bold red]")
        console.print(f"Time taken: {end_time} seconds")
    else:
        list_fonts = fonts.split(',')
    
        table = Table(box=None)
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Value", style="white")
        
        for font_name in list(set(list_fonts)):
            table.add_row(
                "font-family", font_name.replace(
                    '"', ''
                )
            )
        
        table.caption = f"Time taken: {end_time} seconds"
        console.print(table)
