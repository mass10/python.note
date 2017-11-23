#!/usr/bin/env python3
# coding: utf-8
# アヤメデータを可視化します。

import itertools
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from sklearn import datasets

def main():

	iris_data = datasets.load_iris()
	features = iris_data['data']
	feature_names = iris_data['feature_names']
	targets = iris_data['target']

	pyplot.figure(figsize=(12, 8))

	for i, (x, y) in enumerate(itertools.combinations(range(4), 2)):
		pyplot.subplot(2, 3, i + 1)
		markers = ((0, '^', 'r'), (1, 'o', 'g'), (2, 'x', 'b'))
		for t, marker, c in markers:
			pyplot.scatter(features[targets == t, x], features[targets == t, y], marker=marker, c=c)
			pyplot.xlabel(feature_names[x])
			pyplot.ylabel(feature_names[y])
			pyplot.autoscale()
			pyplot.grid()

	pyplot.savefig('0001 - アヤメデータセット.png')

main()
