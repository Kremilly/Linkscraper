#!/usr/bin/python3

import requests, time
import pyperclip as Pyperclip

from http import HTTPStatus

from utils.file import File
from utils.file_ext import FileExt

from classes.env import Env
from layout.layout import Layout

from helper.apis import Apis
from helper.configs import Configs

class Imgur:

    @classmethod
    def get_title(cls, title):
        if not title:
            return f'Screenshot made by {Configs.APP_NAME}'
            
        return title

    @classmethod
    def embed_code(cls, params):
        Layout.header_section("Embed codes")
        Layout.print("[italic yellow]Imgur Post[/italic yellow]:", f'<blockquote class="imgur-embed-pub" lang="en" data-id="{params["imgur_code_url"]}"><a href="{FileExt.remove(params["imgur_page"])}">{cls.get_title(params["title"])}</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>')
        
        Layout.print("[italic yellow]HTML[/italic yellow]:", f"<img src='{params['direct_link']}' alt='{cls.get_title(params['title'])}'/>")
        Layout.print("[italic yellow]Markdown[/italic yellow]:", f"![{cls.get_title(params['title'])}]({params['direct_link']})")
        Layout.print("[italic yellow]BBCode[/italic yellow]:", f"[img]{params['direct_link']}[/img]")

    @classmethod
    def upload(cls, file, title):
        Layout.separator()
        key = Env.get("IMGUR_CLIENT_API")

        if not key:
            return Layout.error("Key is required", False, True, {
                "style": "bold blue",
                "text": "Get your client id here:",
                "value": Apis.IMGUR_API_KEY_URL,
            })
            
        start_time = time.time()
        
        response = requests.request("POST", Apis.IMGUR_API_REQUEST, headers = {
            'Authorization': f"Client-ID {key}"
        }, data = {
            'image': File.to_base64(file),
        })
        
        if response.status_code != HTTPStatus.OK:
            return Layout.error(f"{response.status_code} - Failed to upload image to Imgur.", False, True)

        callback = response.json()
        if callback["success"] == True:
            direct_link = callback['data']['link']
            imgur_page = direct_link.replace("i.", "")
            imgur_code_img = FileExt.remove(imgur_page).replace("https://imgur.com/", "")

            Layout.print("Imgur page:", FileExt.remove(imgur_page), "bold blue")
            Layout.print("Link Direct:", imgur_page, "bold blue")

            cls.embed_code({
                'title': title,
                'imgur_page': imgur_page,
                'direct_link': direct_link,
                'imgur_code_url': imgur_code_img,
            })

            Layout.separator()
            Pyperclip.copy(direct_link)
            
            Layout.print(None, f"Link copied to clipboard", "cyan")
            Layout.time_taken(start_time, True)
            
            return True
        
        Layout.error(f"{callback['status']} - {callback['data']['error']}", False, True)
        return False
