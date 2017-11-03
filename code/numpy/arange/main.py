#!/usr/bin/env python3
# coding: utf-8

import numpy

def main():

	# -100 から 100 まで、7刻みの整数を配列に
	array1 = numpy.arange(-100, 100, 7)

	# shows:
	# [-100  -93  -86  -79  -72  -65  -58  -51  -44  -37  -30  -23  -16   -9   -2
    #     5   12   19   26   33   40   47   54   61   68   75   82   89   96]
	print(array1)

main()
