#!/usr/bin/env python3
# coding: utf-8

import sklearn.datasets

def main():

	iris_data = sklearn.datasets.load_iris()
	print(iris_data['DESCR'])
	return
	
main()
