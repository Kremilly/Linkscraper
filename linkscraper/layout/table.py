#!/usr/bin/python3

from rich.console import Console
from rich.table import Table as RichTable

class Table:
    
    table = RichTable(box=None)
    console = Console(record=True)
    
    @classmethod
    def header(cls, headers):
        for header in headers:
            text = header[0]
            style = header[1]
            no_wrap = header[2]
            
            if style:
                cls.table.add_column(text, style=f"{style}", no_wrap=no_wrap)
            else:
                cls.table.add_column(text, no_wrap=no_wrap)
                
    @classmethod  
    def row(cls, *args):
        cls.table.add_row(*args)
    
    @classmethod    
    def caption(cls, text):
        cls.table.caption = text

    @classmethod
    def display(cls):
        cls.console.print(cls.table)
