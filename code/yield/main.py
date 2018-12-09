#!/usr/bin/env python3
# coding: utf-8

import sys
import inspect

def _log(*args):

	curframe = inspect.currentframe()
	calframe = inspect.getouterframes(curframe, 2)
	caller = calframe[1][3]
	print("[TRACE] <", caller, "> ", *args, sep="")

def _enumeration():

	_log("いまから \"1\" を返します。")
	yield(u'1')

	_log("いまから \"2\" を返します。")
	yield(u'2')

	_log("いまから \"3\" を返します。")
	yield(u'3')

	_log("いまから \"あいうえお\" を返します。")
	yield(u'あいうえお')

	_log("返すものはありません。")

def _main():

	_log("### start ###")
	for e in _enumeration():
		_log("CURRENT: [", e, "]")
	_log("--- end ---")

_main()
