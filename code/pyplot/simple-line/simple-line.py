#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot

def main():

	matplotlib.pyplot.rcParams['font.family'] = 'IPAPGothic'

	matplotlib.pyplot.plot([1,2,3,4])
	matplotlib.pyplot.ylabel('たてじく')
	# matplotlib.pyplot.show()
	matplotlib.pyplot.savefig("simple.png")

main()
