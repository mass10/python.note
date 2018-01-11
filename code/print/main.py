#!/usr/bin/env python
# coding: utf-8

import sys

def println(*args):

	# for Python 2
	for e in args:
		sys.stdout.write(e)
	sys.stdout.write("\n")

	# for Python 3
	print(*args, sep="")

def main():

	println("[info] ", "文字列", "を", "くっつけて", "print")

main()

