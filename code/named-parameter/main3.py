#!/usr/bin/env python3
# coding: utf-8

def _case3(left, right=""):

	print("[TRACE] left=[", left, "], right=[", right, "]", sep="")

def _main():

	_case3(left="LEFT")
	_case3(right="RIGHT", left="LEFT")

_main()

