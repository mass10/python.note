#!/usr/bin/env python
# coding: utf-8

import io
import os
import uuid
import sys
import codecs
import json
import datetime
import uuid
import urllib2
import requests

class out:

	@staticmethod
	def println(*args):

		writer = codecs.getwriter('utf-8')(sys.stdout)
		for x in args:
			t = type(x)
			if t is int:
				writer.write(str(x))
			elif t is str:
				writer.write(x)
			elif t is unicode:
				writer.write(x)
			else:
				writer.write(str(x))
		writer.write("\n")

class global_integer:

	__core = {}

	@staticmethod
	def increment(key):

		if not global_integer.__core.has_key(key):
			global_integer.__core[key] = 1
			return

		global_integer.__core[key] = global_integer.__core[key] + 1

	@staticmethod
	def put(key, value):

		if not global_integer.__core.has_key(key):
			global_integer.__core[key] = value
			return
		current_value = global_integer.__core[key]
		if value <= current_value:
			return False
		global_integer.__core[key] = value
		return True

	@staticmethod
	def current(key):

		if not global_integer.__core.has_key(key):
			return 0
		return global_integer.__core[key]

class main:

	@staticmethod
	def import_content(id, line, content):

		fields = {}
		# fields['id'] = str(uuid.uuid1())
		fields['category'] = id
		fields['line'] = line
		fields['content'] = content
		# content = json.dumps(fields, ensure_ascii=False)
		content = '[' + json.dumps(fields) + ']'
	
		headers = {'Content-type': 'application/json'}
	
		# overwrite=true というものがある？？
		response = requests.post(
			# 'http://127.0.0.1:8983/solr/lcdd/update?commit=true',
			'http://127.0.0.1:8983/solr/lcdd/update',
			headers = headers,
			data = content)

		out.println(response.text)

	@staticmethod
	def name_of_path(path):

		pos = path.rfind('/')
		if pos == -1:
			return ''
		return path[pos + 1:]

	@staticmethod
	def _regist(path):

		# 名前部分
		name = main.name_of_path(path)
		if name == '':
			return
		if name == 'LICENSE.txt':
			return
		if name == 'CHANGES.txt':
			return
		if name == 'README.txt':
			return

		file = io.open(path, mode = 'r', encoding = 'utf-8')

		# 一括読み込み
		# line = file.read()
		# length = len(line)
		# if global_integer.put(u'文章の長さ', length):
		# 	print(length)

		# 1行ずつ読み込んでデータベースに保管
		position = 0
		while True:
			line = file.readline()
			if line == '':
				break
			line = line.rstrip("\r\n")
			main.import_content(name, position, line)
			position += 1
		file.close()

		global_integer.increment(u'文書の数')

	@staticmethod
	def enumerate_documents(path):

		if os.path.isdir(path):
			for x in os.listdir(path):
				main.enumerate_documents(os.path.join(path, x))
		elif os.path.exists(path):
			main._regist(path)
		else:
			print('unknown path [' + path + '].')

	@staticmethod
	def _main():

		start_time = datetime.datetime.now()
		main.enumerate_documents('text/dokujo-tsushin')
		main.enumerate_documents('text/it-life-hack')
		main.enumerate_documents('text/kaden-channel')
		main.enumerate_documents('text/livedoor-homme')
		main.enumerate_documents('text/movie-enter')
		main.enumerate_documents('text/peachy')
		main.enumerate_documents('text/smax')
		main.enumerate_documents('text/sports-watch')
		main.enumerate_documents('text/topic-news')
		out.println(u'[INFO] 文書の数: ', global_integer.current(u'文書の数'))
		end_time = datetime.datetime.now()
		out.println(u'[INFO] 処理時間: ', end_time - start_time)

main._main()


