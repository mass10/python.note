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
	def enum_indices():

		fields = {}
		fields['q'] = '*:*'
		fields['wt'] = 'json'
		
		response = requests.get(
			'http://127.0.0.1:8983/solr/lcdd/select',
			params=fields)
		
		out.println(response.text)

	@staticmethod
	def _main():

		start_time = datetime.datetime.now()
		main.enum_indices()
		end_time = datetime.datetime.now()
		out.println(u'[INFO] 処理時間: ', end_time - start_time)

main._main()


