#!/usr/bin/env python
# coding: utf-8
#
# MySQL で接続する例
#
#
#

import os
import sys
import logging
import MySQLdb







###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class out:

	@staticmethod
	def println(*arguments):

		xwrite = sys.stdout.write
		for x in arguments:
			xwrite(('' + x).encode('utf-8'))
		xwrite("\n")





###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class main:

	@staticmethod
	def _test_mysql():

		connection = MySQLdb.connect(
			host = '192.168.40.129',
			db = 'mysql',
			user = 'root',
			passwd = '').cursor()

		if not connection.execute('SELECT CURRENT_TIMESTAMP'):
			return

		res = connection.fetchall()

		for row in res:
			logging.info(row[0])

		connection.close()

	@staticmethod
	def _main():

		# logging.basicConfig(
		#	filename='myapp.log',
		#	level=logging.INFO)

		logging.basicConfig(
			level=logging.DEBUG)

		logging.info(u'### start ###')
		logging.debug(u'ddddddddddddddddddddddddddddddddddddd')

		main._test_mysql()

		logging.info(u'日本語')
		logging.warn(u'ああああああああああああああああああああああああああ')
		logging.error(u'いいいいいいいいいいいいいいいいいいいいいいいいいいい')
		logging.info(u'--- end ---')

main._main()






