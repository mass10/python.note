#!/usr/bin/env python
# coding: utf-8

from couchbase.bucket import *
import uuid

def _insert(bucket, user_name):

	new_id = user_name
	new_entry = {'user_name': user_name}
	bucket.insert(new_id, new_entry)

def _main():

	b = Bucket('couchbase://127.0.0.1/USERS')
	insert = lambda user_name: _insert(b, user_name)
	insert(u'岸部シロー')
	insert(u'岸部一徳')
	insert(u'沢田研二')
	insert(u'加橋かつみ')
	insert(u'森本太郎')
	insert(u'瞳みのる')

_main()

