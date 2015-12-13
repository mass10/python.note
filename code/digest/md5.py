#!/usr/bin/env python
# coding: utf-8
#
#
# MD5 のサンプル
#
#
#
#
#
#
#

import sys
import codecs
import hashlib

def _println(*args):

	out = codecs.getwriter('utf-8')(sys.stdout)
	for x in args:
		if type(x) is int:
			out.write(str(x))
		else:
			out.write('' + x)
	out.write("\n")

def _main(*arguments):

	e = 'abcdefg'
	if 2 <= len(arguments):
		e = arguments[1]
	g = hashlib.md5()
	g.update(e)
	_println('', e, ': [', g.hexdigest(), ']')
	
_main(*sys.argv)

