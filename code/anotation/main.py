#!/usr/bin/env python3
# coding: utf-8

import mylib.decorator

@mylib.decorator.mydecorator
def _main():
	print("### start ###")
	print("--- end ---")

_main()
