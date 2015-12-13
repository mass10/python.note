#!/usr/bin/env python
# coding: utf-8

def _get_result_by_tuple():

    return 200, 'hello world!'

def _test_01():

    status, content = _get_result_by_tuple()

    print '{}, {}'.format(status, content)

def _main():
	
	_test_01()

_main()
