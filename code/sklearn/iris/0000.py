#!/usr/bin/env python3
# coding: utf-8
#
# 「実践 機械学習システム」より
#

import itertools
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import sklearn.datasets
import numpy as np

def main():

	data = sklearn.datasets.load_iris()

	features = data['data']
	feature_names = data['feature_names']
	target = data['target']
	target_names = data['target_names']
	labels = target_names[target]

	markers = ((0, '^', 'r'), (1, 'o', 'g'), (2, 'x', 'b'))
	for t, marker, c in markers:
		plt.scatter(features[target == t, 0], features[target == t, 1], marker=marker, c=c)

	# 同じ
	# plt.scatter(features[target == 0, 0], features[target == 0, 1], marker='^', c='r')
	# plt.scatter(features[target == 1, 0], features[target == 1, 1], marker='o', c='g')
	# plt.scatter(features[target == 2, 0], features[target == 2, 1], marker='x', c='b')

	plt.savefig('0000.png')

main()
