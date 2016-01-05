#!/usr/bin/env python
# coding: utf-8

import cx_Oracle

def _main():

	# connection = cx_Oracle.connect('USER_NAME/PASSWORD@127.0.0.1:1521')
	# connection = cx_Oracle.connect('USER_NAME/PASSWORD@127.0.0.1:1521/XE')
	connection = cx_Oracle.connect('sys/root@localhost:1521/XE', mode = cx_Oracle.SYSDBA)
	print connection.version

	cursor = connection.cursor()
	cursor.execute('ALTER SESSION SET NLS_DATE_FORMAT = \'YYYY-MM-DD HH24:MI:SS\'')
	cursor.execute('ALTER SESSION SET NLS_TIME_FORMAT = \'HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIME_TZ_FORMAT = \'HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIMESTAMP_FORMAT = \'YYYY-MM-DD HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIMESTAMP_TZ_FORMAT = \'YYYY-MM-DD HH24:MI:SSXFF\'')

	cursor.execute('SELECT CURRENT_TIMESTAMP FROM DUAL')
	for row in cursor.next():
		print row
	cursor.close()

	connection.close()

_main()

