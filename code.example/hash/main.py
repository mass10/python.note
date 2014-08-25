#!/usr/bin/env python
# coding: utf-8
#
#
# digest のサンプル
#
#
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
		out.write('' + x)
	out.write("\n")

def main():

	# =========================================================================
	# MD5 DIGEST
	# =========================================================================
	if True:

		g = hashlib.md5()
		g.update('abcdefg')
		_println('[', g.hexdigest(), ']')
	
	# =========================================================================
	# SHA-256
	# =========================================================================
	if True:

		g = hashlib.sha256()
		g.update('abcdefg')
		_println('[', g.hexdigest(), ']')

main()

