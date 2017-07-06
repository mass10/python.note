#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import codecs

class out:

	@staticmethod
	def println(*arguments):

		# Python3 になったら日本語をそのまま扱えるっぽい
		out = sys.stdout
		# out = codecs.getwriter('utf-8')(sys.stdout)
		for x in arguments:
			if x is None:
				continue
			out.write(str(x))
		out.write("\n")

def _main():

	out.println("### start ###")

	#
	# 初期化
	#
	s = set([9, 8, 20, 1, 5, 3, 2, 3, 4, 5, 5, 2, 1, 2, 4, 0, 3, 2, 1])

	out.println(s)

	#
	# s の型を調べる
	#
	out.println('type(s): [', type(s), ']')
	if type(s) is set:
		out.println('s は set です')
	else:
		print('s は set ではありません')

	#
	# 要素を調べる
	#
	if 5 in s:
		print('s は 5 を持っています')
	else:
		print('s は 5 を持っていません。')

	#
	# 要素を調べる
	#
	if -12 in s:
		print('s は -12 を持っています')
	else:
		print('s は -12 を持っていません。')

	for e in s:
		print(e)

	out.println('--- end ---')

_main()

