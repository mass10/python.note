#!/usr/bin/env python3
# coding: utf-8

import sys
import os

def _enum(path):

	if os.path.isdir(path):
		for x in os.listdir(path):
			_enum(os.path.join(path, x))

	elif os.path.exists(path):
		print("[TRACE] parent: [", os.path.dirname(path), "], name: [", os.path.basename(path), "], ext: [", os.path.splitext(path)[1], "]", sep="")

def main(*args):

	if len(args) == 1:
		return

	path = args[1]

	_enum(path)

main(*sys.argv)
