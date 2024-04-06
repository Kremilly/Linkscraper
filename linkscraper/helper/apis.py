#!/usr/bin/python3

from enum import Enum

class Apis(Enum):

    IP_API_REQUEST = 'http://ip-api.com/json/'
    IMGUR_API_REQUEST = 'https://api.imgur.com/3/image'
    VIRUSTOTAL_API_REQUEST = 'https://www.virustotal.com/api/v3/urls'
    GOOGLE_FONTS_API_REQUEST = 'https://www.googleapis.com/webfonts/v1/webfonts'
    THREATCROWD_API_REQUEST = 'http://ci-www.threatcrowd.org/searchApi/v2/domain/report'

    IMGUR_API_KEY_URL = 'https://api.imgur.com/oauth2/addclient'
    VIRUSTOTAL_API_KEY_URL = 'https://www.virustotal.com/gui/my-apikey'
    GOOGLE_FONTS_API_KEY_URL = 'https://console.cloud.google.com/apis/credentials'
