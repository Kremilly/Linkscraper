#!/usr/bin/python3

from utils.url import URL

from layout.layout import Layout

from core.headers import Headers
from core.cookies import Cookies
from core.scraper import Scraper

from core.static.js import JS
from core.static.css import CSS
from core.static.images import Images

from core.core import Core
from core.plugins import Plugins

from core.write_env import WriteEnv

class Startup:
    
    @classmethod
    def __init__(cls, args):
        cls.args = args
    
    @classmethod
    def run(cls):
        Layout.header()

        if cls.args.write_env:
            return WriteEnv.run()
            
        base_url = cls.args.url
        URL.check_url_and_connection(base_url)

        Core.home(base_url)
        
        match (cls.args.action):
            case '' | 'get-core' | 'core':
                Core.basic(base_url)
            case 'get-headers' | 'headers':
                Headers.section(base_url, cls.args.filter)
            case 'get-cookies' | 'cookies':
                Cookies.section(base_url, cls.args.filter)
            case 'get-js-files' | 'js-files':
                JS.section(base_url, *cls.args)
            case 'get-css-files' | 'css-files':
                CSS.section(base_url, cls.args.show_minify_files, cls.args.filter, cls.args.download)
            case 'get-images-files' | 'images-files':
                Images.section(base_url, cls.args.filter, cls.args.download)
            case 'get-links' | 'links':
                Scraper.section_links(base_url, cls.args.only_external_links, cls.args.show_status_code, cls.args.filter)
            case 'get-emails' | 'emails':
                Scraper.section_emails(base_url, cls.args.filter)
            case 'get-plugins' | 'plugins':
                Plugins.run(cls.args.plugin, base_url, cls.args)
            case _:
                Layout.error('Action invalid', True, True)
