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
	#
	#
	if 1:
		s = {
			u'key1': u'あいうえお'
		}
		_println(s)

	#
	# 部分文字列の取り出し
	#
	if 1:
		s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		_println(s[4:6])

main()
