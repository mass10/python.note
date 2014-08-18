#!/usr/bin/env python
# coding: utf-8
#
#
# ディレクトリ走査
#
#
#
#

import sys
import os

def _enum(path):

	if os.path.isdir(path):
		for x in os.listdir(path):
			_enum(os.path.join(path, x))
	elif os.path.exists(path):
		print(path)
	else:
		print('unknown path [' + path + '].')

def main(*args):

	if len(args) == 1:
		return

	path = args[1]

	_enum(path)

main(*sys.argv)
