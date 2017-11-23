#!/usr/bin/env python3
# coding: utf-8

import sys

def _get_printer(stream):

    def _print(x):
        stream.write(x)
        stream.write("\n")
    return _print

def _main():

    print_line = _get_printer(sys.stdout)
    print_line("こにちは")
    print_line("Ok.")

    # NameError: name '_print' is not defined
    # _print("test")

_main()
