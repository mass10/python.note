#!/usr/bin/env python3
# coding: utf-8

import pandas

def _main():

	records = pandas.read_csv('records.tsv', delimiter="\t")

	#
	# 丸ごと表示
	#
	print(records)

	#
	# 1行ずつ表示
	#
	# ※もしかしたら普通はこういうことをしないのかもしれない
	#
	row_count = len(records.index)
	for i in range(0, row_count):
		print(records.values[i])

_main()

