#!/usr/bin/env python
# coding: utf-8

import sys
import io
import time
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch
import json

def _main(argv):

	index_name = 'idol-index-2015' # must be lower-case.
	doc_type_name = 'idol',



	es = Elasticsearch(host = '127.0.0.1')

	if es.indices.exists(index = index_name):
		es.indices.delete(index = index_name)

	file = io.open('girls.json', encoding = 'utf-8')

	while True:
		line = file.readline()
		line = line.rstrip()
		if line == '':
			break;
		entry = json.loads(line)
		es.index(
			index = index_name,
			doc_type = doc_type_name,
			id = str(uuid.uuid1()),
			body = entry)

	file.close()

	# 強制コミット？
	es.indices.refresh(index = index_name)

_main(sys.argv)
