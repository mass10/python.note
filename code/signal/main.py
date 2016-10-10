#!/usr/bin/env python
# coding: utf-8

import signal
import time

__alive = True

def _alive():

	return __alive

def _handler(signum, frame):

	global __alive

	__alive = False

	print '$$$ interrupt $$$'

def _main():

	print '### start ###'

	signal.signal(signal.SIGINT, _handler)

	while _alive():
		time.sleep(1)

	print '--- end ---'

_main()

