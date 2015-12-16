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

	INDEX_NAME = 'sample_database_20151123'
	DOC_TYPE_NAME = 'sample_entry_20151123',



	# 接続設定
	es = Elasticsearch(host = '127.0.0.1')

	# 全件検索
	# response = es.search(index = INDEX_NAME, body = {})
	response = es.search(index = INDEX_NAME, body={"query": {"match_all": {}}, "size": 9999})

	# 結果を表示
	for e in response['hits']['hits']:
		print json.dumps(e)

	# ヒット数
	print('hits: {0}'.format(response['hits']['total']))

_main(sys.argv)
