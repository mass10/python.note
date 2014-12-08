#!/usr/bin/env python
# coding: utf-8
#
# Python で乱数
#
#
#

import random
import json

def main():
	
	dim = {}

	#
	# gen
	#
	for n in range(100):

		key = random.randint(0, 10)

		if not dim.has_key(key):
			dim[key] = 0
		dim[key] = dim[key] + 1

	#
	# summary
	#
	print json.dumps(dim, sort_keys=True, indent=4)

main()

