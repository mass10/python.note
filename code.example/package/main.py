#!/usr/bin/env python
# coding: utf-8
import sys
import MyPackage
import AnotherPackage
import AnotherPackage.Package1

def _main():

	AnotherPackage.Package1.Logger.println('### start ###')

	if 1:

		#
		# カレントディレクトリのパッケージ内クラスをインスタンス化してメンバ呼び出し
		#

		x = MyPackage.mypackage()
		x.hello()

	if 1:

		#
		# 他のパッケージ内クラスの静的メンバを呼び出す
		#

		AnotherPackage.Package1.Package1.hello()
	
	if 1:

		#
		# 他のパッケージ内のクラスを利用する
		#

		p = AnotherPackage.Package1.Package2()
		p.hello()

	AnotherPackage.Package1.Logger.println('--- end ---')

_main()

