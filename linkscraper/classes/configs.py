#!/usr/bin/python3

from enum import Enum

class Configs(Enum):
    
    VERSION = '2.5.3'
    
    APP_NAME = 'Linkscraper'
    
    HOMEPAGE = 'https://github.com/Kremilly/linkscraper'
    
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    LIST_HTTP_STATUS = 'https://gist.githubusercontent.com/kremilly/31aed3c28577f78bcaace2a377f8aa17/raw/4e765d040b739f0d7bc60ef8c2c8f37c17eae81c/http-status-code.json'
    LIST_COUNTRIES = 'https://gist.githubusercontent.com/kremilly/c468fb230d6fcf97de827e37f91f2f6c/raw/3e037cefa50d0381956e862de478c5e5cce758ab/countries.json'
    LIST_LANGUAGES = 'https://gist.githubusercontent.com/kremilly/fd5e5dd45d3480a8da57d56218cecd1e/raw/221c38e4a7e83e2bb9bab92cd8101c9c9adebaaf/languages.json'
    
    ALLOWED_EXT = [
        '.js', 'min.js',                                    # JS
        '.css', '.min.css',                                 # CSS
        
        '.png',                                             # PNG
        '.gif',                                             # GIF
        '.svg',                                             # SVG
        '.tiff',                                            # TIFF
        '.webp',                                            # WebP
        '.avif',                                            # AVIF
        '.jpeg', '.jpg',                                    # JPEG
        '.jxr', '.wdp', '.hdp',                             # JPEG XR
        '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2',     # JPEG 2000
    ]
