#!/usr/bin/env python
# coding: utf-8

import sys
import urllib

def _main(args):

	p = ''
	if 1 < len(args):
		p = args[1]
	print urllib.quote(p)

_main(sys.argv)

