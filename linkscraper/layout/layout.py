#!/usr/bin/python3

import time, sys, pyfiglet

from rich.prompt import Prompt
from rich.console import Console

from classes.configs import Configs

class Layout:
    
    prompt = Prompt
    console = Console(record=True)
    
    @classmethod
    def separator(cls):
        cls.console.print("-" * 60)
    
    @classmethod
    def header(cls):
        cls.console.print("[bold blue]" + pyfiglet.figlet_format(Configs.APP_NAME.value) + "[/bold blue]")
    
        cls.separator()
        cls.console.print(f"Homepage: [bold green]{Configs.HOMEPAGE.value}[/bold green]")
        cls.separator()

        cls.console.print(f"\t\tv.[bold green]{Configs.VERSION.value}[/bold green]")
        cls.separator()
    
    @classmethod  
    def success(cls, text, separator = False):
        if separator: cls.separator()
        cls.console.print(f"[bold green]Success[/bold green]: {text}")
    
    @classmethod 
    def error(cls, error, separator = False, exit = False, additional_print = None):
        if separator: cls.separator()
        
        cls.console.print(f"[bold red]Error[/bold red]: {error}")
        
        if additional_print:
            cls.print(
                additional_print["text"],
                additional_print["value"],
                additional_print["style"],
            )
        
        if exit: sys.exit()
    
    @classmethod  
    def header_section(cls, text):
        cls.separator()
        cls.console.print(f"{text}")
        cls.separator()
    
    @classmethod
    def print(cls, text, value, style=None, separator = False):
        if separator: cls.separator()
        
        if not text == None:
            if style:
                cls.console.print(text, f"[{style}]{value}[/{style}]")
            else:
                cls.console.print(text, value)
        else:
            cls.console.print(f"[{style}]{value}[/{style}]")
    
    @classmethod      
    def time_taken(cls, start_time, separator = False):
        if separator: cls.separator()
        
        end_time = "{:.2f}".format(time.time() - start_time)
        cls.print("Time taken:", f"{end_time} seconds")
    
    @classmethod
    def header_plugin(cls, plugin):
        cls.header_section(f"Plugin: [bold cyan]{plugin}[/bold cyan]")
