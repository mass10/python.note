#!/usr/bin/env python
# coding: utf-8

from couchbase.bucket import *
import uuid

def _insert(bucket, user_name):

	new_id = user_name
	new_entry = {'user_name': user_name}
	bucket.insert(new_id, new_entry)

def _main():

	users = Bucket('couchbase://127.0.0.1/USERS')

	_insert(users, u'岸部シロー')
	_insert(users, u'岸部一徳')
	_insert(users, u'沢田研二')
	_insert(users, u'加橋かつみ')
	_insert(users, u'森本太郎')
	_insert(users, u'瞳みのる')

_main()

