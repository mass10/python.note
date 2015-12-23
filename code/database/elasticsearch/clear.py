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
		print('削除しました')
	else:
		print('インデックスはきれいな状態です')

_main(sys.argv)
