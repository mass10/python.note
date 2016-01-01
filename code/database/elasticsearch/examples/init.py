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

	# index(=データベース？？)を破棄
	if es.indices.exists(index = INDEX_NAME):
		es.indices.delete(index = INDEX_NAME)

	# index に document(?) を追加
	for e in range(100):
		es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = {})
		print e

	# 強制コミット？？
	es.indices.refresh(index = INDEX_NAME)

_main(sys.argv)
