#!/usr/bin/python3

import requests, time, re

from rich.table import Table
from rich.console import Console

console = Console(record=True)

def plugin_extract_colors(url):
    start_time = time.time()
    
    response = requests.get(url)
    content = response.text

    colors = []
    color_id = 0
    
    patterns = [
        re.compile(r'#[0-9a-fA-F]{6}'),  # e.g., #FFFFFF
        re.compile(r'#[0-9a-fA-F]{3}'),  # e.g., #FFF
        re.compile(r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)'),  # e.g., rgb(255, 255, 255)
        re.compile(r'rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*[\d.]+\s*\)')  # e.g., rgba(255, 255, 255, 0.5)
    ]

    table = Table(box=None)
    table.add_column("#", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    for pattern in patterns:
        colors.extend(
            pattern.findall(content)
        )

    colors = list(set(colors))
    
    if len(colors) > 0:
        for color in colors:
            table.add_row(f"Color #{color_id}", color)
            color_id += 1

    end_time = "{:.2f}".format(time.time() - start_time)
        
    table.caption = f"Total of colors: {len(colors)} - Time taken: {end_time} seconds"
    console.print(table)
