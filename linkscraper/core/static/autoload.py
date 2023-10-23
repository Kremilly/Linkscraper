#!/usr/bin/python3

import requests, time

from utils.utils import *
from classes.configs import *
from utils.utils_http import *
from utils.utils_files import *
from core.download_resources import *

from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from layout.table import Table

session = requests.Session()
session.headers["User-Agent"] = Configs.DEFAULT_USER_AGENT.value
