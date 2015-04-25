#!/usr/bin/env python
# coding: utf-8

import AnotherPackage.Package1

class mypackage:

	def __init__(self):
		AnotherPackage.Package1.Logger.println("mypackage.__init__()")

	@staticmethod
	def hello():
		AnotherPackage.Package1.Logger.println("mypackage.hello()")
