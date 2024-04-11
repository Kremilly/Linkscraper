#!/usr/bin/python3

class Configs:
    
    VERSION = '2.6.6'
    
    APP_NAME = 'Linkscraper'
    
    CONFIGS_FILE = './linkscraper.yml'
    
    HOMEPAGE = 'https://github.com/Kremilly/linkscraper'
    
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
