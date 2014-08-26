#!/usr/bin/env python
# coding: utf-8
#
#
# SQLite3 のデータベースファイルをダンプします。
#
#
#



import sys
import sqlite3
import codecs
import io
import os
import json






def _println(*arguments):

	out = codecs.getwriter('utf-8')(sys.stdout)
	for unknown in arguments:
		out.write('' + unknown)
	out.write("\n")

def _show_records(connection, table_name):

	#
	# BANNER
	#
	_println('-------------------------')
	_println('TABLE: ', json.dumps(table_name))
	_println('-------------------------')

	#
	# 抽出
	#
	rows = connection.execute(
		'select * from "' + table_name + '"')
	detected = 0
	for row in rows:
		_println(json.dumps(row, ensure_ascii=False))
		detected += 1

	#
	# SUMMARY
	#
	_println(u'' + str(detected) + u' 行のレコードを検出しました。')
	_println()

def _dump_db(path):

	if not os.path.isfile(path):
		_println(u'引数はファイルではないようだ...')
		return

	connection = sqlite3.connect(
		path, isolation_level=None)
	rows = connection.execute(
		'select name from sqlite_master \
		where type = ? order by name',
		['table'])
	for row in rows:
		_show_records(connection, row[0])

	if 0:
		connection.execute(
			'update auth_user set email = ? where id = ?',
			['unknown@example.com', 1])
	if 0:
		connection.execute(
	 		'update app1_person set mail = ?',
	 		['unknown@example.com'])

	connection.close()

def main(*args):

	if len(args) == 1:
		_println(u'引数は？')
		return

	path = unicode(args[1], 'utf-8')

	_println('### start ###')

	if not os.path.isfile(path):
		_println(u'引数はファイルではないようだ...')
		return

	# =========================================================================
	# データベースファイル全体をダンプ
	# =========================================================================
	_dump_db(path)

	_println('--- end ---')

main(*sys.argv)
