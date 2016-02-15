#!/usr/bin/env python
# coding: utf-8

import requests
import json

def _main():

	parameters = {'q': '*', 'wt': 'json'}
	response = requests.get(
		'http://localhost:8983/solr/exampledocs/select',
		params = parameters)
	data = json.loads(response.text, encoding = 'utf-8')
	print data[u'responseHeader']
	print data[u'response']

_main()

