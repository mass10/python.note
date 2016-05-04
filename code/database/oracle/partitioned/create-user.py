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
	cursor.execute('CREATE USER TEST IDENTIFIED BY password DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS')
	cursor.execute('GRANT CREATE SESSION TO TEST')
	cursor.execute('GRANT CREATE ANY TABLE, SELECT ANY TABLE, UPDATE ANY TABLE, DELETE ANY TABLE, INSERT ANY TABLE TO TEST')
	connection.close()
	print 'Ok.'

_main()
