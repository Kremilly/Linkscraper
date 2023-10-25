#!/usr/bin/python3

import requests
from classes.configs import Configs

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

        r = requests.get(Configs.LIST_COUNTRYS.value)
        r = r.json()

        for code in r:
            if code['alpha2'] == country:
                return code['name']

    @classmethod
    def language(cls, lang):
        lang = cls.get_param(lang, 0)

        r = requests.get(Configs.LIST_LANGUAGES.value)
        r = r.json()

        for code in r:
            if code['code'] == lang:
                return code['name']
