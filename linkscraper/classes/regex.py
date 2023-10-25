#!/usr/bin/python3

from enum import Enum

class Regex(Enum):
    
    COLORS_CODE = [
        r'#[0-9a-fA-F]{6}', # e.g., #FFFFFF
        r'#[0-9a-fA-F]{3}', # e.g., #FFF
        r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)', # e.g., rgb(255, 255, 255)
        r'rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*[\d.]+\s*\)', # e.g., rgba(255, 255, 255, 0.5)
    ]
    
    URL_PATTERN_PROTOCOL = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    URL_PATTERN_CHECK_PROTOCOL = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
