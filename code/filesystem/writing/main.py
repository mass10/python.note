#!/usr/bin/env python3
# coding: utf-8

import os
import io
import sys
import codecs


def _main(argv):

    stream = io.open("log", "a+", encoding="utf-8")
    stream.write("AAAAAA\n")
    stream.write("あいうえお\n")
    stream.close()

_main(sys.argv)

