#!/usr/bin/env python3
# coding: utf-8

import numpy

def main():

	print('--- 0～1までの乱数を1つ生成 ---')
	print(numpy.random.rand())

	print('')
	print('--- 0～1までの乱数を10個生成 ---')
	print(numpy.random.rand(10))

	print('')
	print('--- 0～1までの乱数を2列x10行生成 ---')
	print(numpy.random.rand(10, 2))

main()
