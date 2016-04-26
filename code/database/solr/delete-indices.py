#!/usr/bin/env python
# coding: utf-8

import io
import os
import uuid
import sys
import codecs
import json
import datetime
import requests




class out:

	@staticmethod
	def _str(x):

		if x is None:
			return ''
		t = type(x)
		if t is int:
			return str(x)
		if t is long:
			return str(x)
		if t is float:
			return str(x)
		if t is str:
			return x
		if t is unicode:
			return x
		return str(x)

	@staticmethod
	def println(*args):

		writer = codecs.getwriter('utf-8')(sys.stdout)
		for x in args:
			writer.write(out._str(x))
		writer.write("\n")

class main:

	@staticmethod
	def delete_indices():

		fields = {}
		fields['delete'] = {'query': '*'}
		fields['wt'] = 'json'

		headers = {'Content-Type': 'application/json'}

		response = requests.post(
			'http://127.0.0.1:8983/solr/lcdd/update?commit=true',
			headers = headers,
			params = fields)
		
		out.println(response.text)

	@staticmethod
	def _main():

		start_time = datetime.datetime.now()
		main.delete_indices()
		end_time = datetime.datetime.now()
		out.println(u'[INFO] 処理時間: ', end_time - start_time)

main._main()
