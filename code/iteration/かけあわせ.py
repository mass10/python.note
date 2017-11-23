#!/usr/bin/env python3
# coding: utf-8
import itertools

def main():

	print('# 単純な 0, 1, 2, 3')
	for x in range(4):
		print(x)

	print('')
	print('# (0, 1, 2, 3) による総当たり')
	for x, y in itertools.combinations([0, 1, 2, 3], 2):
		print('({}, {})'.format(x, y))

	print('')
	print('# (0, 1, 2, 3) による総当たり、インデックス添え')
	for i, (x, y) in enumerate(itertools.combinations([0, 1, 2, 3], 2)):
		print('{}:({}, {})'.format(i, x, y))

main()
