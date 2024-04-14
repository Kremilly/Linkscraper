#!/usr/bin/python3
 
from helper.configs import Configs

from classes.startup import Startup

if __name__ == '__main__':
    Startup('E.g.: python linkscraper -u http://example.com', [
        {'short': 'u', 'long': 'url', 'help': 'URL to scan', 'required': False},
        {'short': 'f', 'long': 'filter', 'help': 'Filter data', 'required': False},
        {'short': 'a', 'long': 'action', 'help': 'Run an action', 'required': False},
        {'short': 'p', 'long': 'plugin', 'help': 'Load a plugin', 'required': False},
        {'short': 'b', 'long': 'browser', 'help': 'Set browser to take screenshot', 'required': False},
        {'short': 't', 'long': 'title', 'help': 'Set title the screenshot on Imgur', 'required': False},
        {'short': 'd', 'long': 'download', 'help': 'Download static files', 'action': 'store_true', 'required': False},
        {'short': 'up', 'long': 'upload', 'help': 'Upload the screenshot to Imgur', 'action': 'store_true', 'required': False},
        {'short': 'v', 'long': 'version', 'help': 'Show current version', 'action': 'version', 'version': f'{Configs.VERSION}'},
        {'short': 'we', 'long': 'write-env', 'help': 'Write environments file (.env)', 'action': 'store_true', 'required': False},
        {'short': 'ssc', 'long': 'show-status-code', 'help': 'Show status code', 'required': False, 'action': 'store_true', 'default': 'false'},
        {'short': 'smf', 'long': 'show-minify-files', 'help': 'Show only minify files', 'required': False, 'action': 'store_true', 'default': 'false'},
        {'short': 'oel', 'long': 'only-external-links', 'help': 'Show only external links', 'required': False, 'action': 'store_true', 'default': 'false'},
    ]).run()
