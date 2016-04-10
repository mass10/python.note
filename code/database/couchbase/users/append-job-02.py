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
	update = lambda user_name, birthplace:\
		_update(b, user_name, u'job', birthplace)
	update(u'岸部シロー', [u'ザ・タイガース', u'俳優'])
	update(u'岸部一徳', [u'ザ・タイガース', u'俳優'])
	update(u'沢田研二', [u'ザ・タイガース', u'歌手'])
	update(u'加橋かつみ', u'ザ・タイガース')
	update(u'森本太郎', u'ザ・タイガース')
	update(u'瞳みのる', [u'ザ・タイガース', u'中国文学・中国語研究者', u'高等学校教諭'])

_main()

