#!/usr/bin/env python
# coding: utf-8

from couchbase.bucket import *
import datetime

def _update(bucket, user_name, attribute_name, value):

	e = bucket.get(user_name)
	if e == None:
		return
	e.value[attribute_name] = value
	bucket.upsert(user_name, e.value)

def _main():

	b = Bucket('couchbase://127.0.0.1/USERS')
	update = lambda user_name, birth: \
		_update(b, user_name, u'birth', unicode(birth))
	update(u'岸部シロー', datetime.datetime(1949, 6, 7))
	update(u'岸部一徳', datetime.datetime(1947, 1, 9))
	update(u'沢田研二', datetime.datetime(1948, 6, 25))
	update(u'加橋かつみ', datetime.datetime(1948, 2, 4))
	update(u'森本太郎', datetime.datetime(1946, 11, 18))
	update(u'瞳みのる', datetime.datetime(1946, 9, 22))

_main()

