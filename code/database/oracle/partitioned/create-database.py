#!/usr/bin/env python
# coding: utf-8

import cx_Oracle
import uuid

def _open_connection():

	connection = cx_Oracle.connect('TEST/password@localhost:1521/XE')
	cursor = connection.cursor()
	cursor.execute('ALTER SESSION SET NLS_DATE_FORMAT = \'YYYY-MM-DD HH24:MI:SS\'')
	cursor.execute('ALTER SESSION SET NLS_TIME_FORMAT = \'HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIME_TZ_FORMAT = \'HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIMESTAMP_FORMAT = \'YYYY-MM-DD HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET NLS_TIMESTAMP_TZ_FORMAT = \'YYYY-MM-DD HH24:MI:SSXFF\'')
	cursor.execute('ALTER SESSION SET TIME_ZONE = \'Asia/Tokyo\'')
	return connection

def _drop_table():

	connection = _open_connection()
	cursor = connection.cursor()
	try:
		sql = '''
			DROP TABLE TEST01
		'''
		cursor.execute(sql)
	except:
		pass
	cursor.close()
	connection.close()

def _create_database():

	connection = _open_connection()
	cursor = connection.cursor()

	sql = '''
		CREATE TABLE TEST01(
			"ID" NVARCHAR2(256) NOT NULL,
			"DATE" DATE NOT NULL,
			PRIMARY KEY("ID")
		)
		PARTITION BY RANGE("DATE") INTERVAL(NUMTODSINTERVAL(1, 'DAY'))
		(PARTITION VALUES LESS THAN (TO_DATE('2002-01-01','YYYY-MM-DD')))
	'''

	cursor.execute(sql)

	new_id = unicode(uuid.uuid4())
	sql = '''
		INSERT INTO TEST01("ID", "DATE") VALUES(:id, CURRENT_TIMESTAMP)
	'''
	cursor.execute(sql, id = new_id)

	sql = '''
		SELECT * FROM TEST01
	'''
	cursor.execute(sql)
	for e in cursor.fetchall():
		print 'FETCH:', e[0], ',', e[1]

	cursor.close()
	connection.close()

def _main():

	_create_database()
	_drop_table()

_main()
