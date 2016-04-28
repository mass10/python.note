#!/usr/bin/env python
# coding: utf-8
#
# 2016-04-28 Bot をつくろうとして Functions App になったやつ
#
#

import io
import requests
import json
import urllib


def _get_function_url():

	with io.open('.url') as file:
		url = file.readline()
		url = url.rstrip()
		return url

def _main():

	parameters = {
		'name': u'東郷平八郎'.encode('utf-8')
	}
	url = _get_function_url() + '&' + urllib.urlencode(parameters)
	response = requests.get(url)
	if not response.ok:
		return response.text
	print(response.text)

_main()



