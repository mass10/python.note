#!/usr/bin/env python
# coding: utf-8
#

import sys
import time
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch
import json

def _main(argv):

	INDEX_NAME = 'idle_database_2015'
	DOC_TYPE_NAME = 'idle_entry',

	es = Elasticsearch(host = '192.168.141.160')
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = { 'name': u'槙田紗子', 'birthplace': u'神奈川県' })
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = { 'name': u'根岸愛', 'birthplace': u'埼玉県' })
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = { 'name': u'増井みお', 'birthplace': u'東京都' })
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = { 'name': u'峯岸みなみ', 'birthplace': u'東京都' })
	es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = { 'name': u'武藤彩未', 'birthplace': u'東京都' })

	es.indices.refresh(index = INDEX_NAME)
	response = es.search(index = INDEX_NAME, body = {})
	print('hits: {0}'.format(response['hits']['total']))
	for e in response['hits']['hits']:
		print json.dumps(e, ensure_ascii = False)
	es.indices.delete(index = INDEX_NAME)

_main(sys.argv)
