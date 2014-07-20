#!/usr/bin/env python
# coding: utf-8

import sys

class Package1:

	def __init__(self):
		Logger.println("Package1.__init__()")

	@staticmethod
	def hello():
		Logger.println("Package1.hello()")

class Package2:

	def __init__(self):
		Logger.println("Package2.__init__()")

	def hello(self):
		Logger.println("Package2.hello()")

class Logger:

	@staticmethod
	def println(*argv):
		for e in argv:
			sys.stdout.write(str(e))
		sys.stdout.write("\n")
