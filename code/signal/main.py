#!/usr/bin/env python
# coding: utf-8

import signal
import time

__alive = True

def _handler(signum, frame):

	__alive = False

	print '$$$ interrupt $$$'

        raise Exception('INTERRUPT')
	
def _main():

	print '### start ###'

	signal.signal(signal.SIGINT, _handler)

	while __alive:
		time.sleep(1)

	print '--- end ---'

_main()

