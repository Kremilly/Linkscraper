#!/usr/bin/python3

import requests

from classes.settings import Settings

class Locale:

    @classmethod
    def get_param(cls, string, slice):
        if string.find("_") != -1:
            return string.split("_")[slice].lower()
        else:
            return string.lower()
    
    @classmethod
    def country(cls, country):
        country = cls.get_param(country, 1)

        r = requests.get(Settings.get('dataset.list_countries', 'STRING'))
        r = r.json()

        for code in r:
            if code['alpha2'] == country:
                return code['name']

    @classmethod
    def language(cls, lang):
        lang = cls.get_param(lang, 0)

        r = requests.get(Settings.get('dataset.list_languages', 'STRING'))
        r = r.json()

        for code in r:
            if code['code'] == lang:
                return code['name']
