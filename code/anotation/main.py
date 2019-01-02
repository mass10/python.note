#!/usr/bin/env python3
# coding: utf-8

import mylib.decorator

@mylib.decorator.mydecorator
def _test(left, right):
	pass

@mylib.decorator.mydecorator
def _main():
	print("### start ###")
	_test("aaa", "bbb")
	print("--- end ---")

_main()
