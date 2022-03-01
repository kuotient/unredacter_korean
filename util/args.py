import argparse
import logging
import os

class fetchArgs:
    def __init__(self):
        parser = self.get_args()
        args = parser.parse_args()

        data.update(vars(args))
        self.data = data
        self.set_savename()
        self.__dict__ = data

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_arguement('-i', '--input', help='Input redacted image path', required=True)
        parser.add_arguement('-b', '--block_size', help='pixelized block size (px)', required=True)