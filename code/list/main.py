#!/usr/bin/env python
# coding: utf-8

def _test_01():

	#
	# list オブジェクト
	#

	values = [
		1,
		233,
		192,
		999,
		{'key-01': 'value-01', 'key-02': 'value-02'},
		1283,
		u'ゆるめるモ！',
		'AKB48',
		'SKE48',
		'NGT48',
		u'乃木坂46',
		u'アップアップガールズ(仮)',
		u'バンドじゃないもん！',
		[901, 902, 903],
		u'あいうえお'
	]

	values.append('----------')

	for e in values:
		print e

def _main():

	_test_01()

_main()
