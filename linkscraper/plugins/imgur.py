#!/usr/bin/python3

import requests, pyperclip, time

from utils.utils import *
from utils.utils_files import *

from classes.env import Env
from layout.layout import Layout
from classes.configs import Configs

def get_title(title):
    if not title:
        return f'Screenshot made by {Configs.APP_NAME.value}'
    else:
        return title
    
def embed_code(imgur_code_img, direct_link, imgur_page, title):
    Layout.header_section("Embed codes")
    
    Layout.print("[italic yellow]Imgur Post[/italic yellow]:", f'<blockquote class="imgur-embed-pub" lang="en" data-id="{imgur_code_img}"><a href="{remove_extension(imgur_page)}">{get_title(title)}</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>')
    
    Layout.print("[italic yellow]HTML[/italic yellow]:", f"<img src='{direct_link}' alt='{get_title(title)}'/>")
    Layout.print("[italic yellow]Markdown[/italic yellow]:", f"![{get_title(title)}]({direct_link})")
    Layout.print("[italic yellow]BBCode[/italic yellow]:", f"[img]{direct_link}[/img]")

def plugin_imgur(file, title):
    Layout.separator()
    key = Env.get("IMGUR_CLIENT_API")

    if not key:
        Layout.error("Key is required", False, True, {
            "text": "Get your client id here:",
            "value": "https://api.imgur.com/oauth2/addclient",
            "style": "bold green"
        })
    else:
        start_time = time.time()
        
        response = requests.request("POST", "https://api.imgur.com/3/image", headers = {
            'Authorization': f"Client-ID {key}"
        }, data = {
            'image': to_base64(file),
            'title': get_title(title)
        })

        callback = response.json()
        if callback["success"] == True:
            direct_link = callback['data']['link']
            imgur_page = direct_link.replace("i.", "")
            imgur_code_img = remove_extension(imgur_page).replace("https://imgur.com/", "")

            Layout.print("Imgur page:", remove_extension(imgur_page), "bold green")
            Layout.print("ILink Direct:", imgur_page, "bold green")

            embed_code(imgur_code_img, direct_link, imgur_page, title)

            Layout.separator()
            pyperclip.copy(direct_link)
            
            Layout.print(None, f"Link copied to clipboard", "cyan")
            Layout.time_taken(start_time, True)
        else:
            Layout.error(f"{callback['status']} - {callback['data']['error']}", False, True)
