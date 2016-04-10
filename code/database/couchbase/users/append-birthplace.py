#!/usr/bin/env python
# coding: utf-8

from couchbase.bucket import *

def _update(bucket, user_name, attribute_name, value):

	e = bucket.get(user_name)
	if e == None:
		return
	e.value[attribute_name] = value
	bucket.upsert(user_name, e.value)

def _main():

	b = Bucket('couchbase://127.0.0.1/USERS')
	update = lambda user_name, birthplace: \
		_update(b, user_name, u'birthplace', birthplace)
	update(u'岸部シロー', u'京都府京都市')
	update(u'岸部一徳', u'京都府京都市')
	update(u'沢田研二', u'鳥取県鳥取市')
	update(u'加橋かつみ', u'大阪府堺市')
	update(u'森本太郎', u'京都府京都市')
	update(u'瞳みのる', u'京都府')

_main()

