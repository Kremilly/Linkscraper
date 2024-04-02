#!/usr/bin/python3

import argparse

class Flags:
    
    @classmethod
    def parser(cls, desc, arguments):
        parser = argparse.ArgumentParser(description=desc)

        for arg in arguments:
            short_ = '-' + arg.pop('short', None)
            long_ = '--' + arg.pop('long', None)
            
            parser.add_argument(short_, long_, **arg)

        args = parser.parse_args()

        return args
