#!/usr/bin/env python3
# coding: utf-8

def _sub(**arg):

	# right
	assert(type(arg) is dict)
	print("row: {}, col: {}".format(arg["row"], arg["col"]))

def _main():

	_sub(row=10, col=3)

_main()



