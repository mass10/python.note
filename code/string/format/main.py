#!/usr/bin/env python
# coding: utf-8

import sys

def _println(*xx):
	for x in xx:
		if x is None:
			continue
		sys.stdout.write(str(x))
	sys.stdout.write("\n")

def main():

	#
	# LEGACY(?) FORMATTING
	#
	print '%d' % 999
	print '%s, %d' % ('ABC', 999)

	#
	# MODERN(?) FORMATTING
	# Python 2.6 系まで
	#
	print '{0}, {1}'.format('ABC', 999)

	#
	# MODERN(?) FORMATTING
	# Python 2.7 移行はインデックスが省略可能になった
	#
	print '{}, {}'.format('ABC', 999)

main()
