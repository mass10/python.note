#!/usr/bin/env python3
# coding: utf-8

import pandas
import matplotlib
matplotlib.use("Agg")
# matplotlib.matplotlib_fname()

def _main():

	# return
	t = pandas.read_table("type-02.tsv",
		usecols=["DATE", "COUNT"], index_col=["DATE"], parse_dates=["DATE"])

	print(t.index)
	print(t.columns)
	print(t)

	axis = t.plot(title="monthly active users", figsize=(7, 4))
	# matplotlib.pyplot.rcParams["font.family"] = "IPAGothic"
	# matplotlib.pyplot.rcParams["font.family"] = "IPAMincho"
	# matplotlib.pyplot.rcParams["font.family"] = "IPAexGothic"
	matplotlib.pyplot.rcParams["font.family"] = "IPAPGothic"
	axis.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
	axis.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
	matplotlib.pyplot.ylim(ymin=0)
	matplotlib.pyplot.savefig("type-02.png")

_main()
