#!/usr/bin/env python
# coding: utf-8

import sys

def _println(*arguments):

	for unknown in arguments:
		sys.stdout.write((u'' + unknown).encode(u'utf-8'))
	sys.stdout.write(u"\n")

def _enumeration():

	yield(u'1')
	yield(u'2')
	yield(u'3')
	yield(u'あいうえお')

def Main():

	_println(u'### start ###')

	for unknown in _enumeration():
		_println(u'[', unknown, u']')

	_println(u'--- end ---')

Main()
