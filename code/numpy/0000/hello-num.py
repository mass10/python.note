#!/usr/bin/env python
# coding: utf-8

import os
import sys
import codecs
import numpy

class Main:

	def main(self):

		print(numpy.version.full_version)

		xar = numpy.array([1, 2, 3, 4, 5])
		print(xar)
		print(xar.ndim)
		print(xar.shape)

		print('Ok.')

Main().main()
