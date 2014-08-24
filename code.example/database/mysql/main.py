#!/usr/bin/env python
# coding: utf-8
#
#
#
# Python から mysql-connector-python を使用する
#
#
#
#
#
#
#

import sys
import os
import mysql.connector
import codecs




def _println(*args):

	out = codecs.getwriter('utf-8')(sys.stdout)
	for unknown in args:
		out.write(unknown)
	out.write('\x0a')

def main():

	_println('### start ###')

	connection = None
	cursor = None

	try:

		_println('let\'s connect')

		connection = mysql.connector.connect(
				host='192.168.141.139',
				user='root',
				# password='root',
				database='information_schema')

		cursor = connection.cursor()

		cursor.execute(
			'SELECT TABLE_CATALOG,\
			TABLE_SCHEMA,\
			TABLE_NAME,\
			TABLE_TYPE,\
			ENGINE,\
			VERSION,\
			ROW_FORMAT,\
			TABLE_ROWS,\
			TABLE_COMMENT FROM tables')

		for row in cursor:
			_println(str(row))

	except Exception as e:

		_println(str(e))

	if cursor is not None:
		cursor.close()
	if connection is not None:
		connection.close()

	_println('--- exit ---')

main()

