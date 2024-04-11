import time, requests

from http import HTTPStatus

from helper.apis import Apis

from classes.env import Env

from classes.settings import Settings

from utils.http import HTTP
from utils.file import File
from utils.date_time import DateTime
from utils.file_size import FileSize

from layout.table import Table
from layout.layout import Layout

class GoogleFonts:
    
    @classmethod
    def create_path(cls, path):
        path = f"{Settings.get('storage.downloads', 'string')}/{path}"
        File.create_path(path)
        return path
    
    @classmethod
    def download_font(cls, link, path):
        response = requests.get(link)
        font_path = f"{path + File.get_remote_file_name(link)}"
        File.write(font_path, response.content, 'wb', 'utf-8')
    
    @classmethod
    def get_font_files(cls, font_name):
        key = Env.get("GOOGLE_FONTS_KEY")
        
        if not key:
            Layout.error("Key is required", False, True, {
                "style": "bold blue",
                "text": "Get your key here:",
                "value": Apis.GOOGLE_FONTS_API_KEY_URL,
            })
        else:
            response = requests.get(Apis.GOOGLE_FONTS_API_REQUEST, params={
                "key": key, 
                "sort": "alpha"
            })
            
            if response.status_code != HTTPStatus.OK:
                Layout.error(f"{response.status_code}: {response.reason}", False, True, {
                    "style": "bold blue",
                    "text": "Get your key here:",
                    "value": Apis.GOOGLE_FONTS_API_KEY_URL,
                })

            fonts = response.json().get('items', [])
            for font in fonts:
                if font['family'].lower() == font_name.lower():
                    return font['files']

            return None

    @classmethod
    def get_list(cls, font_name):
        links = cls.get_font_files(font_name)
        
        if links:
            return links
        else:
            return None
    
    @classmethod
    def list(cls, url, font_name, *args):
        start_time = time.time()
        list = cls.get_list(font_name)
        
        Layout.header_section(f"Google Fonts: [bold blue]{font_name}[/bold blue]")
        
        if list is not None:
            if args.download is not False:
                path = cls.create_path(f"{HTTP.get_hostname(url)}/fonts/{font_name}/")
            
            Table.header([
                ("Style", "white", True),
                ("URL", "bold blue", True),
                ("Size", "green", False)
            ])
            
            for style, file_url in list.items():
                Table.row(style, file_url, FileSize.remote_file(file_url))
                
                if args.download is not False:
                    cls.download_font(file_url, path)

            Table.caption(f"Total of variants: {len(list)} - "
                          f"Time taken: {DateTime.calculate_interval(start_time)} seconds")
            
            Table.display()
        else:
            Layout.error("This font is not found on Google Fonts", False, True)
