#!/usr/bin/env python
# coding: utf-8

from couchbase.bucket import *
import json

def _main():

	bucket = Bucket('couchbase://127.0.0.1/USERS')
	result = bucket.query("users", "V_USERS_02", use_devmode = False, limit = 99999, skip = 0)
	for entry in result:
		print json.dumps(entry.value, ensure_ascii = False, sort_keys = True, encoding = 'utf-8')

_main()

