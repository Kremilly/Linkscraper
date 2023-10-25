#!/usr/bin/python3

import requests, time

from classes.configs import *

from utils.file import File
from utils.file_ext import FileExt
from core.download_resources import *

from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from layout.table import Table

session = requests.Session()
session.headers["User-Agent"] = Configs.DEFAULT_USER_AGENT.value
