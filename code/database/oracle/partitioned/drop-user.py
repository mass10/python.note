#!/usr/bin/env python
# coding: utf-8

import cx_Oracle

def _open_connection():

	connection = cx_Oracle.connect('sys/root@localhost:1521/XE', mode = cx_Oracle.SYSDBA)
	cursor = connection.cursor()
	cursor.execute('ALTER SESSION SET NLS_DATE_FORMAT = \'YYYY-MM-DD HH24:MI:SS\'')
	cursor.execute('ALTER SESSION SET NLS_TIME_FORMAT = \'HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIME_TZ_FORMAT = \'HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIMESTAMP_FORMAT = \'YYYY-MM-DD HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIMESTAMP_TZ_FORMAT = \'YYYY-MM-DD HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET TIME_ZONE = \'Asia/Tokyo\'')
	return connection

def _main():

	connection = _open_connection()
	cursor = connection.cursor()
	cursor.execute('DROP USER TEST')
	connection.close()

_main()
