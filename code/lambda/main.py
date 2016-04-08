#!/usr/bin/env python
# coding: utf-8

def _call(func, n):

	print func(n)

def _main():

	func = lambda i: i * i
	for n in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
		_call(func, n)

_main()

