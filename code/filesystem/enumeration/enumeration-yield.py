#!/usr/bin/env python3
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
			for e in _enum(os.path.join(path, x)):
				yield e
	elif os.path.exists(path):
		yield path
	else:
		print('unknown path [' + path + '].')

def main(*args):

	w = stopwatch()
	for path in args:
		for e in _enum(path):
			print("[", e, "]", sep="")
	print(w)

main(*sys.argv[1:])
