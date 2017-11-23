#!/usr/bin/env python3
# coding: utf-8

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot

def main():

	matplotlib.pyplot.rcParams['font.family'] = 'IPAPGothic'
	matplotlib.pyplot.ylabel('たてじく')
	matplotlib.pyplot.xlabel('よこじく')
	matplotlib.pyplot.plot([1,2,3,4])
	# matplotlib.pyplot.show()
	matplotlib.pyplot.savefig("simple.png")

main()
