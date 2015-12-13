#!/usr/bin/env python
# coding: utf-8

import sys
import json

def _println(*xx):

	out = sys.stdout.write

	for x in xx:
		if x is None:
			continue
		elif type(x) is int:
			out(str(x))
		elif type(x) is str:
			out(x)
		elif type(x) is dict:
			out(json.dumps(x, ensure_ascii=False, sort_keys=True))
		elif type(x) is list:
			out(json.dumps(x, ensure_ascii=False, sort_keys=True))
		else:
			out(str(type(x)))

	out("\n")

def _test_20151109():

	s = u'東京都八王子市高尾町 1-1-1'
	print u'"{}" の「八王子」の位置は ({}) です。'.format(s, s.index(u'八王子'))
	s = u'1-1-1, Takaomachi, Hahcioji, Tokyo, Japan'
	print u'"{}" の「1-1-1」の位置は ({}) です。'.format(s, s.index(u'1-1-1'))

def _main():

	#
	# dict の表示
	#
	if True:
		s = {
			u'key-1': u'あいうえお',
			u'key-2': u'東京都八王子市高尾町 1-1-1'
		}
		_println(s)

	#
	# 部分文字列の取り出し
	#
	if True:
		s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		_println(s[4:6])

	if True:
		a = [99999, '東京都八王子市高尾町', 123.4567]
		_println(a);

	# _test_20151109()

_main()
