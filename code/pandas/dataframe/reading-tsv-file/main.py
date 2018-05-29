#!/usr/bin/env python3
# coding: utf-8

import pandas

def _main():

	records = pandas.read_csv('records.tsv', delimiter="\t")
	print(records.columns)
	for i, row in enumerate(records.values):
		print('{}: {}'.format(i, row))

_main()

