#!/usr/bin/env python
# coding: utf-8

import sys

def _main():

	out = sys.stdout.write


	"""
	長いコメント
	長いコメント
	長いコメント
	長いコメント
	長いコメント
	長いコメント
	"""


	out("hello.\n")
	out("コンニチハ.\n")

	samples = (
		'a',
		'b',
		'c'
	)

	for e in samples:

		out('[')
		out(e)
		out(']')
		out("\n")

	pass

_main()












