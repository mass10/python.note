#!/usr/bin/env python
# coding: utf-8

import sys
import os
import io


def _main():

	file = sys.stdin
	while True:
		line = file.readline()
		if line == '':
			break
		line = line.rstrip("\r\n")
		print(u'[{0}]'.format(line))
	file.close()

_main()

