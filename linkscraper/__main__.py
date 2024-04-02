#!/usr/bin/python3

import sys

from utils.url import URL

from core.write_env import WriteEnv

from layout.layout import Layout

from core.headers import Headers
from core.cookies import Cookies
from core.scraper import Scraper

from core.static.js import JS
from core.static.css import CSS
from core.static.images import Images

from core.core import Core
from core.plugins import Plugins

from classes.flags import Flags
from classes.configs import Configs

args = Flags.parser('Example of use: python linkscraper -u http://example.com', [
    {'short': 'u', 'long': 'url', 'help': 'URL to scan', 'required': False},
    {'short': 'a', 'long': 'action', 'help': 'Run an action', 'required': False},
    {'short': 'p', 'long': 'plugin', 'help': 'Load a plugin', 'required': False},
    {'short': 'f', 'long': 'filter', 'help': 'Filter data', 'required': False},
    {'short': 'b', 'long': 'browser', 'help': 'Set browser to take screenshot', 'required': False},
    {'short': 't', 'long': 'title', 'help': 'Set title the screenshot on Imgur', 'required': False},
    {'short': 'd', 'long': 'download', 'help': 'Download static files', 'action': 'store_true', 'required': False},
    {'short': 'up', 'long': 'upload', 'help': 'Upload the screenshot to Imgur', 'action': 'store_true', 'required': False},
    {'short': 'v', 'long': 'version', 'help': 'Show current version', 'action': 'version', 'version': f'{Configs.VERSION.value}'},
    {'short': 'we', 'long': 'write-env', 'help': 'Write environments file (.env)', 'action': 'store_true', 'required': False},
    {'short': 'ssc', 'long': 'show-status-code', 'help': 'Show status code', 'required': False, 'action': 'store_true', 'default': 'false'},
    {'short': 'smf', 'long': 'show-minify-files', 'help': 'Show only minify files', 'required': False, 'action': 'store_true', 'default': 'false'},{'short': 'oel', 'long': 'only-external-links', 'help': 'Show only external links', 'required': False, 'action': 'store_true', 'default': 'false'},
])

if __name__ == "__main__":
    Layout.header()

    if args.write_env:
        WriteEnv.run()
        sys.exit()
        
    BASE_URL = args.url
    URL.check_url_and_connection(BASE_URL)

    Core.home(BASE_URL)
    
    match (args.action):
        case '' | 'get-core' | 'core':
            Core.basic(BASE_URL)
        case 'get-headers' | 'headers':
            Headers.section(BASE_URL, args.filter)
        case 'get-cookies' | 'cookies':
            Cookies.section(BASE_URL, args.filter)
        case 'get-js-files' | 'js-files':
            JS.section(BASE_URL, args.show_minify_files, args.filter, args.download)
        case 'get-css-files' | 'css-files':
            CSS.section(BASE_URL, args.show_minify_files, args.filter, args.download)
        case 'get-images-files' | 'images-files':
            Images.section(BASE_URL, args.filter, args.download)
        case 'get-links' | 'links':
            Scraper.section_links(BASE_URL, args.only_external_links, args.show_status_code, args.filter)
        case 'get-emails' | 'emails':
            Scraper.section_emails(BASE_URL, args.filter)
        case 'get-plugins' | 'plugins':
            Plugins.run(args.plugin, BASE_URL, args.browser, args.upload, args.title, args.google_fonts, args.download)
        case _:
            Layout.error('Action invalid', True, True)
