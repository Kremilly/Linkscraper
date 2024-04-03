#!/usr/bin/python3

import argparse

class Flags:
    
    @classmethod
    def parser(cls, desc, arguments):
        parser = argparse.ArgumentParser(description=desc)

        for arg in arguments:
            parser.add_argument(
                f"-{arg.pop('short', None)}", f"--{arg.pop('long', None)}", **arg
            )

        return parser.parse_args()
