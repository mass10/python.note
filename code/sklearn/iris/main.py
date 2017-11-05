#!/usr/bin/env python3
# coding: utf-8

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot
import sklearn.datasets

def main():

	data = sklearn.datasets.load_iris()
	features = data.data[:, [0, 2]]
	matplotlib.pyplot.scatter(*features.T, c=[['#203070', '#9090b0', '#505070'][x] for x in data.target])
	matplotlib.pyplot.show()
	matplotlib.pyplot.savefig('tmp.png')

main()
