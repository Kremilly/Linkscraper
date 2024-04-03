#!/usr/bin/python3

import time
from datetime import datetime

class DateTime:
    
    @classmethod
    def get_datetime(cls):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    @classmethod
    def today_datetime(cls):
        return datetime.today().strftime("%a, %b %d %Y - %I:%M:%S %p")
    
    @classmethod
    def calculate_interval(cls, start_time):
        return '{:.2f}'.format(time.time() - start_time)
