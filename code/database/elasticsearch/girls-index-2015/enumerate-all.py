#!/usr/bin/env python
# coding: utf-8

from elasticsearch import Elasticsearch
import json

def _main():

	index_name = 'idol-index-2015'

	es = Elasticsearch(host = '127.0.0.1')

	if not es.indices.exists(index_name):
		print('INDEX:{0} が存在しません'.format(index_name))
		return

	response = es.search(
		index = index_name,
		body = {'query': {'match_all': {}}, 'size': 9999})

	for e in response['hits']['hits']:
		print json.dumps(
			e,
			ensure_ascii = False,
			sort_keys = True,
			indent = 4)

	print('hits: {0}'.format(response['hits']['total']))

_main()
