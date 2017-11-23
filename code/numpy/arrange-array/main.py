#!/usr/bin/env python3
# coding: utf-8

import numpy

def 行を結合する():

	print('# 行の結合(縦の結合)')
	array1 = numpy.array([
		[100, 200, 300],
		[101, 202, 303],
		[105, 220, 331]])
	array2 = numpy.array([
		[133, 230, 311],
		[109, 227, 321],
		[105, 270, 397]])
	array3 = numpy.concatenate([array1, array2])
	print(array3)
	print('{} 行のレコード'.format(len(array3)))

def 列を結合する():

	print()
	print('# 列の結合(横の結合)')
	array1 = numpy.array([
		[100, 200, 300],
		[101, 202, 303],
		[105, 220, 331]])
	array2 = numpy.array([
		[500, 600, 700],
		[501, 602, 703],
		[505, 620, 731]])
	array3 = numpy.c_[array1, array2]
	print(array3)
	print('{} 行のレコード'.format(len(array3)))

def main():

	行を結合する()
	列を結合する()

main()
