#!/usr/bin/env python3
# coding: utf-8

import sklearn.datasets
import pandas
import numpy

def _main():

	# configure
	pandas.set_option('display.width', 100)
	pandas.set_option('display.max_columns', 99)
	pandas.set_option('display.max_rows', 9999)

	# load
	iris_data = sklearn.datasets.load_iris()
	features = iris_data['data']
	feature_names = iris_data['feature_names']
	target_names = iris_data['target_names']
	targets = iris_data['target']

	# convert
	table = pandas.DataFrame(data=features, columns=feature_names)

	# adding columns
	table['target'] = targets
	table['target_name'] = target_names[targets]

	# filtering
	print(table.query("target == 0"))
	print(table.query("target == 1"))
	print(table.query("target == 2"))

	# summary
	print('{} 件のレコードを表示'.format(len(table)))

_main()
