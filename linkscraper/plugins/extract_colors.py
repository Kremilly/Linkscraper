#!/usr/bin/python3

import requests, time, re
from layout.table import Table

from classes.regex import Regex

from utils.date_time import DateTime

class ExtractColors:
    
    @classmethod
    def run(cls, url):
        start_time = time.time()
        
        response = requests.get(url)
        content = response.text

        colors = []
        color_id = 0
        
        patterns = [
            re.compile(Regex.COLORS_CODE.value[0]),  # e.g., #FFFFFF
            re.compile(Regex.COLORS_CODE.value[1]),  # e.g., #FFF
            re.compile(Regex.COLORS_CODE.value[2]),  # e.g., rgb(255, 255, 255)
            re.compile(Regex.COLORS_CODE.value[3])  # e.g., rgba(255, 255, 255, 0.5)
        ]
        
        Table.header([
            ("#", "cyan", True),
            ("Value", "white", False)
        ])

        for pattern in patterns:
            colors.extend(
                pattern.findall(content)
            )

        colors = list(set(colors))
        
        if len(colors) > 0:
            for color in colors:
                Table.row(f"Color #{color_id}", color)
                color_id += 1

        Table.caption(f"Total of colors: {len(colors)} - Time taken: {DateTime.calculate_interval(start_time)} seconds")
        Table.display()
