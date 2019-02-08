#!/usr/bin/env python3
# coding: utf-8

import datetime

def show_now():

	now = datetime.datetime.now()
	print("[TRACE] now is ", now, sep="")
	print("[TRACE] now is ", "{0:%Y-%m-%d %H:%M:%S.%f}".format(now), sep="")
	print("[TRACE] now is ", "{0:%F}".format(now), sep="")

def show_mktime():

	timestamp = datetime.datetime.strptime('2012/01/01 20-29-39', "%Y/%m/%d %H-%M-%S")
	print("[TRACE] timestamp is ", timestamp, sep="")

def main():

	show_now()
	show_mktime()

main()

