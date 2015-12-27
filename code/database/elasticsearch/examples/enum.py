#!/usr/bin/env python
# coding: utf-8
#
# elasticsearch はじめの一歩 with Python
#
#
# pip install elasticsearch
#

import sys
import time
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch
import json

def _main(argv):

	index_name = 'sample_database_20151123'
	if 2 <= len(argv):
		index_name = argv[1]

	# 接続設定
	es = Elasticsearch(host = '127.0.0.1')

	if not es.indices.exists(index_name):
		print('INDEX:{0} が存在しません'.format(index_name))
		return

	# 全件検索
	# response = es.search(index = index_name, body = {}) # returns 10 indices.
	response = es.search(index = index_name, body={"query": {"match_all": {}}, "size": 99999})

	# 結果を表示
	for e in response['hits']['hits']:
		print json.dumps(e, ensure_ascii=False, sort_keys=True)

	# ヒット数
	print('hits: {0}'.format(response['hits']['total']))

_main(sys.argv)
