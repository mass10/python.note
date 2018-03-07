#!/usr/bin/env python3
# coding: utf-8
#
# elasticsearch はじめの一歩 with Python
#
#
# pip3 install elasticsearch
#

import sys
import time
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch
import json


INDEX_NAME = 'ゲームインデックス'
DOC_TYPE_NAME = 'ゲーム',

def _setup():

	es = Elasticsearch(host = '127.0.0.1')
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "いっき", "maker": "サンソフト"})
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "ツインビー", "maker": "コナミ"})
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "スペランカー", "maker": "アイレム"})
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "ゼビウス", "maker": "ナムコ"})
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "ディグダグ", "maker": "ナムコ"})
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "謎の村雨城", "maker": "コナミ"})
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = uuid.uuid4(), body = {"name": "ゼルダの伝説", "maker": "任天堂"})
	# 強制コミット
	es.indices.refresh(index = INDEX_NAME)

def _search1():

	print("$$$ search1 $$$")
	es = Elasticsearch(host = '127.0.0.1')
	query = {
		"query": {
			"match": {
				"maker": "ナムコ"
			}
		},
		"size": 9999
	}
	response = es.search(index = INDEX_NAME, doc_type = "ゲーム", body=query)
	for e in response['hits']['hits']:
		print(json.dumps(e, ensure_ascii = False))
	print('hits: {0}'.format(response['hits']['total']))

def _search2():

	print("$$$ search2 $$$")
	es = Elasticsearch(host = '127.0.0.1')
	query = {
		"query": {
			"match": {
				"maker": "ナムコ"
			}
		}
	}
	response = es.search(index = INDEX_NAME, doc_type = "人名", body=query)
	for e in response['hits']['hits']:
		print(json.dumps(e, ensure_ascii = False))
	print('hits: {0}'.format(response['hits']['total']))

def _search3():

	print("$$$ search2 $$$")
	es = Elasticsearch(host = '127.0.0.1')
	query = {
		"query": {
			"match": {
				"メーカー": "ナムコ"
			}
		}
	}
	response = es.search(index = INDEX_NAME, doc_type = "ゲーム", body=query)
	for e in response['hits']['hits']:
		print(json.dumps(e, ensure_ascii = False))
	print('hits: {0}'.format(response['hits']['total']))

def _fin():

	es = Elasticsearch(host = '127.0.0.1')
	# index(=データベース)を破棄
	if es.indices.exists(index = INDEX_NAME):
		es.indices.delete(index = INDEX_NAME)

def _main(argv):

	_setup()

	_search1()
	_search2()
	_search3()

	_fin()

_main(sys.argv)
