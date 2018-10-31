#!/usr/bin/env python3
# coding: utf-8

import random
from sklearn.metrics import jaccard_similarity_score

def _main():

	base = list(range(0, 30))

	SIZE = 30

	x = random.sample(base, k=SIZE)
	print('x: ', x)

	y = random.sample(base, k=SIZE)
	print('y: ', y)

	result = jaccard_similarity_score(x, y)
	print(result, "\n")

_main()

