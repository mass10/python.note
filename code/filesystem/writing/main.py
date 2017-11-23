#!/usr/bin/env python3
# coding: utf-8

import os
import io
import sys
import codecs


def _main(argv):

    stream = io.open("test.log", "a+")
    stream.write("AAAAAA\n")
    stream.write("あいうえお\n")
    stream.close()

_main(sys.argv)

