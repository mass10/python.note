#!/usr/bin/env python
# coding: utf-8

import sys

def _enumeration():

	yield(u'1')
	yield(u'2')
	yield(u'3')
	yield(u'あいうえお')

def Main():

	for e in _enumeration():
		print e

Main()
