#!/usr/bin/env python3
# coding: utf-8

import sys
import sqlite3
import codecs
import io
import os
import json

class out:

	@staticmethod
	def println(*arguments):
		print(*arguments, sep="")

class application:

	_connection = None
	_path = None

	def __init__(self, path):

		self._connection = None
		self._path = path

	def _open(self):

		if self._connection is not None:
			return self._connection
		self._connection = sqlite3.connect(self._path, isolation_level=None)
		return self._connection

	def show_records(self):

		print('*** dump ***')
		connection = self._open()
		rows = connection.execute('SELECT * FROM T_USER')
		detected = 0
		for row in rows:
			out.println(json.dumps(row, ensure_ascii=False))
			detected += 1

	def drop_user_table(self):

		print('*** drop ***')
		connection = self._open()
		try:
			table_exists = False
			result = connection.execute('SELECT * FROM SQLITE_MASTER WHERE TYPE = ? AND NAME = ?', ['table', 'T_USER'])
			for row in result:
				table_exists = True
			if not table_exists:
				return
			result = connection.execute('DROP TABLE T_USER')
			out.println(result)
		except Exception as e:
			out.println('[ERROR] ', e)

	def create_database(self):

		print('*** create ***')
		connection = self._open()
		try:
			sql = 'CREATE TABLE T_USER(UID NVARCHAR, USER_NAME NVARCHAR, BIRTH TIMESTAMP, ADDRESS NVARCHAR)'
			result = connection.execute(sql)
			out.println(result)
			sql = 'INSERT INTO T_USER(UID, USER_NAME, BIRTH, ADDRESS) VALUES(?, ?, ?, ?)'
			result = connection.execute(sql, ['kabuwee', 'kweet abwee', '2017-01-02', '東京都大田区蒲田4-1-3 中央ビル 3F'])
			out.println(result)
		except Exception as e:
			out.println('[ERROR] ', e)

	def free(self):

		out.println('*** free ***')
		if self._connection is None:
			return
		self._connection.close()
		self._connection = None

def main(*args):

	app = application('test.db')
	try:
		app.drop_user_table()
		app.create_database()
		app.show_records()
	finally:
		app.free()

main(*sys.argv)
