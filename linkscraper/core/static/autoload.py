#!/usr/bin/python3

import requests, time

from classes.configs import Configs

from utils.file import File
from utils.file_ext import FileExt
from utils.file_size import FileSize
from core.download_resources import DownloadResources

from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from layout.table import Table
from layout.layout import Layout

session = requests.Session()
session.headers["User-Agent"] = Configs.DEFAULT_USER_AGENT.value
