#!/usr/bin/python3

import argparse

from utils.url import URL

from core.write_env import WriteEnv

from layout.layout import Layout
from classes.configs import Configs

from core.headers import Headers
from core.cookies import Cookies
from core.scraper import Scraper

from core.static.js import JS
from core.static.css import CSS
from core.static.images import Images

from core.core import Core
from core.plugins import Plugins

parser = argparse.ArgumentParser(description="Example of use: python linkscraper -u http://example.com")

parser.add_argument("-u", "--url", help="URL to scan", required=False)
parser.add_argument("-a", "--action", help="Run an action", required=False)
parser.add_argument("-p", "--plugin", help="Load a plugin", required=False)
parser.add_argument("-filter", "--filter", help="Filter data", required=False)
parser.add_argument("-b", "--browser", help="Set browser to take screenshot", required=False)
parser.add_argument("-t", "--title", help="Set title the screenshot on Imgur", required=False)
parser.add_argument("-d", "--download", help="Download static files", action="store_true", required=False)
parser.add_argument("-up", "--upload", help="Upload the screenshot to Imgur", action="store_true", required=False)
parser.add_argument("-dvc", "--device", help="Set device type for Google Lighthouse", required=False, default="desktop")
parser.add_argument("-gf", "--google-fonts", help="Download fonts from Google Fonts", action="store_true", required=False)
parser.add_argument("-version", "--version", help="Show current version", action="version", version=Configs.VERSION.value)
parser.add_argument("-write-env", "--write-env", help="Write environments file (.env)", action="store_true", required=False)
parser.add_argument("-ssc", "--show-status-code", help="Show status code", action="store_true", required=False, default="false")
parser.add_argument("-smf", "--show-minify-files", help="Show only minify files", action="store_true", required=False, default="false")
parser.add_argument("-oel", "--only-external-links", help="Show only external links", action="store_true", required=False, default="false")

args = parser.parse_args()

if __name__ == "__main__":
    Layout.header()

    if args.write_env:
        WriteEnv.run()
    else: 
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
                JS.section(BASE_URL, args.show_minify_files, args.filter, args.download)
            case 'get-images-files' | 'images-files':
                Images.section(BASE_URL, args.filter, args.download)
            case 'get-links' | 'links':
                Scraper.section_links(BASE_URL, args.only_external_links, args.show_status_code, args.filter)
            case 'get-emails' | 'emails':
                Scraper.section_emails(BASE_URL, args.filter)
            case 'get-plugins' | 'plugins':
                Plugins.run(args.plugin, BASE_URL, args.browser, args.upload, args.title, args.google_fonts, args.download)
            case _:
                Layout.error("Action invalid", True, True)
