#!/usr/bin/env python
# coding: utf-8

import signal
import time

class application:

	def __init__(self):
		self.__alive = True

	def _alive(self):
		return self.__alive

	def run(self):
		print '### start ###'
		while self._alive():
			print '(running...)'
			time.sleep(1)
		print '--- end ---'

	def quit(self):
		self.__alive = False

app = application()

class main:

	@staticmethod
	def _handler(signum, frame):
		app.quit()
		print '$$$ interrupt $$$'

	@staticmethod
	def main():
		signal.signal(signal.SIGINT, main._handler)
		signal.signal(signal.SIGTERM, main._handler)
		app.run()

main.main()
