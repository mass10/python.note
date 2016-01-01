#!/usr/bin/env python
# coding: utf-8
#
# 簡単なファイル入出力
#  http://docs.python.jp/2/library/io.html
#
#

import os
import io


def _main():

	#
	# write
	#

	file = io.open('sample.txt', mode='w', encoding='utf-8')
	file.write(u" こんにちは         \r\n")
	file.write(u"	こんにちは				\n")
	file.write(u"こんにちは 	 	\r\n")
	file.write(u"\n")
	file.close()

	#
	# read
	#

	file = io.open('sample.txt', mode='r', encoding='utf-8')
	while True:
		line = file.readline()
		if line == '':
			break
		line = line.rstrip("\r\n")
		print(u'[{0}]'.format(line))
	file.close()

	#
	# unlink
	#

	os.unlink('sample.txt')

_main()
