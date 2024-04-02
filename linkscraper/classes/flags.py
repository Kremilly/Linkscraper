#!/usr/bin/python3

import argparse

from classes.configs import Configs

class Flags:
    
    @classmethod
    def parser(cls, arguments):
        parser = argparse.ArgumentParser(description="Example of use: python linkscraper -u http://example.com")

        for arg in arguments:
            short_ = '-' + arg.pop('short', None)
            long_ = '--' + arg.pop('long', None)
            
            parser.add_argument(short_, long_, **arg)

        args = parser.parse_args()

        return args
