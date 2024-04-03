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
    def run(cls, plugin, url,args):
        Layout.header_plugin(plugin)

        match (plugin):
            case 'whois':
                Whois.run(url)
            case 'robots':
                Robots.run(url)
            case 'page-details':
                PageDetails.run(url)
            case 'virustotal':
                VT.run(url)
            case 'ip-location':
                IPLocation.run(url)
            case 'screenshot':
                Screenshot.run(url, args)
            case 'detect-fonts':
                DetectFonts.run(url, args)
            case 'extract-colors':
                ExtractColors.run(url)
            case _:
                Layout.error('Plugin invalid', False, True)
