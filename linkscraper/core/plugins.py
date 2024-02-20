#!/usr/bin/python3

from layout.layout import Layout

from plugins.whois import Whois
from plugins.robots import Robots
from plugins.virustotal import VT
from plugins.screenshot import Screenshot
from plugins.ip_location import IPLocation
from plugins.page_details import PageDetails
from plugins.detect_fonts import DetectFonts
from plugins.extract_colors import ExtractColors

class Plugins:

    @classmethod
    def run(cls, plugin, url, browser = None, upload = None, title = None, google_fonts = None, download = None):
        Layout.header_plugin(plugin)

        if plugin == "whois":
            Whois.run(url)
        elif plugin == "robots":
            Robots.run(url)
        elif plugin == "page-details":
            PageDetails.run(url)
        elif plugin == "virustotal":
            VT.run(url)
        elif plugin == "ip-location":
            IPLocation.run(url)
        elif plugin == "screenshot":
            Screenshot.run(url, browser, upload, title)
        elif plugin == "detect-fonts":
            DetectFonts.run(url, google_fonts, download)
        elif plugin == "extract-colors":
            ExtractColors.run(url)
        else:
            Layout.error("Plugin invalid", False, True)
