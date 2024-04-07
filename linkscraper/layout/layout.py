#!/usr/bin/python3

import sys, pyfiglet

from rich.prompt import Prompt
from rich.console import Console

from helper.configs import Configs

from utils.date_time import DateTime

class Layout:
    
    prompt = Prompt
    console = Console(record=True)
    
    @classmethod
    def separator(cls):
        return cls.console.print("-" * 60)
    
    @classmethod
    def header(cls):
        cls.console.print("[bold blue]" + pyfiglet.figlet_format(Configs.APP_NAME) + "[/bold blue]")
    
        cls.separator()
        cls.console.print(f"Homepage: [bold green]{Configs.HOMEPAGE}[/bold green]")
        cls.separator()

        cls.console.print(f"\t\tv.[bold green]{Configs.VERSION}[/bold green]")
        cls.separator()
    
    @classmethod  
    def success(cls, text, separator = False):
        if separator: 
            cls.separator()

        return cls.console.print(f"[bold green]Success[/bold green]: {text}")
    
    @classmethod 
    def error(cls, error, separator = False, exit = False, additional_print = None):
        if separator: 
            cls.separator()
        
        cls.console.print(f"[bold red]Error[/bold red]: {error}")
        
        if additional_print:
            return cls.print(
                additional_print["text"],
                additional_print["value"],
                additional_print["style"],
            )
        
        if exit:
            return sys.exit()
    
    @classmethod  
    def header_section(cls, text):
        cls.separator()
        cls.console.print(f"{text}")
        cls.separator()
    
    @classmethod
    def print(cls, text, value, style = None, separator = False):
        if separator: 
            cls.separator()
        
        if not text == None:
            if style:
                return cls.console.print(text, f"[{style}]{value}[/{style}]")
            
            return cls.console.print(text, value)
        
        return cls.console.print(f"[{style}]{value}[/{style}]")
    
    @classmethod      
    def time_taken(cls, start_time, separator = False):
        if separator: 
            cls.separator()
        
        return cls.print("Time taken:", f"{DateTime.calculate_interval(start_time)} seconds")
    
    @classmethod
    def header_plugin(cls, plugin):
        return cls.header_section(f"Plugin: [bold cyan]{plugin}[/bold cyan]")
