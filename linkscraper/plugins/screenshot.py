#!/usr/bin/python3

import os, time
import random as r
from plugins.imgur import *
from rich.console import Console

from utils.utils import generate_id
from utils.utils_http import get_hostname

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from layout.layout import *

layout = Layout()
console = Console(record=True)

def browser_chrome(url, file):
    options = webdriver.ChromeOptions()
    
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.save_screenshot(file)
    driver.quit()

def browser_firefox(url, file):
    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.save_screenshot(file)
    driver.quit()

def plugin_screenshot(url, browser, upload, title):
    start_time = time.time()
    
    path = f"screenshots\\{get_hostname(url)}\\"
    create_folder(path)

    file = path + f"{get_hostname(url)}-{generate_id()}.png"
    
    if not browser or browser == 'chrome':
        browser_chrome(url, file)
    elif browser == 'firefox':
        browser_firefox(url, file)
    else:
        layout.error("Browser is invalid", False, True)

    if os.path.exists(file):
        layout.success("Success: screenshot saved with successfully.")

        if not upload:
            os.startfile(os.getcwd() + "\\" + file)
            layout.time_taken(start_time)
        else:
            plugin_imgur(file, title)
