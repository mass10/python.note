#!/usr/bin/env python
# coding: utf-8
#
# > before you run
#
#      easy_install requests
#

import requests

def TestGet():

	#
	# GET リクエストを送出します。
	#

	fields = {}
	response = requests.get("http://127.0.0.1/", params=fields)

	print(response.text)

def TestPost():

	#
	# POST リクエストを送出します。
	#

	fields = {}
	fields['login_form.user'] = 'unknown@example.jp';
	fields['login_form.password'] = 'no password';

	response = requests.post("http://127.0.0.1/login", params=fields)

	print(response.text)

def Main():

	TestGet()

	TestPost()

Main()
