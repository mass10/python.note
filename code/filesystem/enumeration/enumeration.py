#!/usr/bin/env python
# coding: utf-8
#
# ディレクトリ走査
#

import sys
import os

import datetime

class stopwatch:

	_value = None

	def __init__(self):
		self._member = datetime.datetime.now()

	def __repr__(self):
		current = datetime.datetime.now()
		elapsed = current - self._member
		return str(elapsed)

def _enum(path):

	if os.path.isdir(path):
		for x in os.listdir(path):
			_enum(os.path.join(path, x))
	elif os.path.exists(path):
		print(path)
	else:
		print('unknown path [' + path + '].')

def main(*args):

	w = stopwatch()
	for path in args:
		_enum(path)
	print(w)
		
main(*sys.argv[1:])
