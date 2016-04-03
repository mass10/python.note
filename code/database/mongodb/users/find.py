#!/usr/bin/env python
# coding: utf-8

import os
import pymongo
import json
import datetime
import time

def _conversion(unknown):

	if isinstance(unknown, datetime.datetime):
		return unknown.isoformat()
	try:
		return str(unknown)
	except:
		raise TypeError(repr(unknown) + " is not JSON serializable")

def _main():

	client = pymongo.MongoClient(['192.168.141.128'], 27017)
	db = client['test']
	collection = db['db20160325']

	while True:

		count = 0

		os.system('clear')

		print('----------------------- {0}'.format(datetime.datetime.now()))

		for e in collection.find():

			# 表示用に _id を消す
			# e['_id'] = "..."
			del e['_id']

			# print json.dumps(e, ensure_ascii=False, sort_keys=True, indent=4, default=_conversion)
			print json.dumps(e, ensure_ascii=False, sort_keys=False, indent=None, default=_conversion, encoding='utf-8')

			count = count + 1

		print '{0} indices found.'.format(count)

		time.sleep(1)

_main()

