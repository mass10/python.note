#!/usr/bin/env python3
# coding: utf-8

import sklearn.datasets
import pandas

def main():

	# アヤメのサンプルデータをテーブル状に表示する
	data = sklearn.datasets.load_iris()
	table = pandas.DataFrame(data.data, columns=data.feature_names)
	print(table)

main()
