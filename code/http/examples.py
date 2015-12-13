#!/usr/bin/env python
# coding: utf-8

import requests

def TestGet():

	fields = {}
	fields['q'] = u'ウェブスクレイピング'
	response = requests.get("http://www.google.com/search", params=fields)
	print(response.text)

def TestPost():

	fields = {}
	fields['login_form.user'] = 'unknown@example.jp'
	fields['login_form.password'] = 'no password'
	response = requests.post("http://127.0.0.1/login", params=fields)
	print(response.text)

def _main():

	TestGet()
	# TestPost()

_main()
