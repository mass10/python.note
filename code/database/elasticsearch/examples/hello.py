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


def _get_insert(connection, index_name, doc_type):
	def _operation(name, maker):
		connection.index(index = index_name, doc_type = doc_type, id = uuid.uuid4(),
			body = {"name": name, "maker": maker})
	return _operation

def _main(argv):

	INDEX_NAME = 'ゲームインデックス'
	DOC_TYPE_NAME = 'ゲーム',

	# 接続設定
	# es = Elasticsearch()
	es = Elasticsearch(host = '127.0.0.1')

	insert = _get_insert(es, INDEX_NAME, DOC_TYPE_NAME)

	# index に document(?) を追加
	insert("いっき", "サンソフト")
	insert("ツインビー", "コナミ")
	insert("スペランカー", "アイレム")
	insert("ゼビウス", "ナムコ")
	insert("ゼビウス", "ナムコ")
	insert("謎の村雨城", "コナミ")
	insert("ゼルダの伝説", "任天堂")

	# 強制コミット
	es.indices.refresh(index = INDEX_NAME)

	# time.sleep(0.5)

	# 全件検索
	# response = es.search(index = INDEX_NAME, body = {})
	response = es.search(
		index = INDEX_NAME,
		body={"query": {"match_all": {}}, "size": 9999})

	# 結果を表示
	for e in response['hits']['hits']:
		print(json.dumps(e, ensure_ascii = False))

	# ヒット数
	print('hits: {0}'.format(response['hits']['total']))

	# index(=データベース？？)を破棄
	if es.indices.exists(index = "人名インデックス"):
		es.indices.delete(index = INDEX_NAME)

_main(sys.argv)
