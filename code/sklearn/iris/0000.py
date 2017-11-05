#!/usr/bin/env python3
# coding: utf-8
#
# 「実践 機械学習システム」より
#

import itertools
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

def main():

	data = load_iris()

	features = data['data']
	feature_names = data['feature_names']
	target = data['target']
	target_names = data['target_names']
	labels = target_names[target]

	set = ((0, "^", "r"), (1, "o", "g"), (2, "x", "b"))
	for t, marker, c in set:
		plt.scatter(features[target == t, 0], features[target == t, 1], marker=marker, c=c)

	# plt.show()
	plt.savefig('0000.png')

main()
