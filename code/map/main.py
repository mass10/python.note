#!/usr/bin/env python
# coding: utf-8

def _bi(x):

	return x * x

def _main():

	#
	# ラムダ式
	#

	list = map(lambda i: i * i, [1, 2, 3, 4, 5])

	print(list)

	#
	# 普通の関数を呼び出す場合
	#

	list = map(_bi, [1, 2, 3, 4, 5])

	print(list)

_main()

