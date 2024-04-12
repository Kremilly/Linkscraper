#!/usr/bin/python3

import time
from datetime import datetime

from classes.settings import Settings

class DateTime:
    
    @classmethod
    def get_datetime(cls):
        return datetime.now().strftime(Settings.get('format_dates.datetime', 'STRING'))
    
    @classmethod
    def today_datetime(cls):
        return datetime.today().strftime(Settings.get('format_dates.today_datetime', 'STRING'))
    
    @classmethod
    def calculate_interval(cls, start_time):
        return '{:.2f}'.format(time.time() - start_time)
