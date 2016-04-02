#!/usr/bin/env python
# coding: utf-8

import riak
import uuid
import datetime
import urllib2

def _update(bucket, user_name, attributes):

	key = urllib2.quote(user_name.encode('utf-8'))
	e = bucket.get(key)
	if e == None:
		return
	for new_key in attributes.keys():
		e.data[new_key] = attributes[new_key]
	e.store()

def _main():

	server = riak.RiakClient(pb_port = 8087)
	bucket = server.bucket(u'The Tigers')
	update = lambda user_name, birth: _update(bucket, user_name, birth)
	update(u'岸部シロー', {u'birth': unicode(datetime.datetime(1949, 6, 7))})
	update(u'岸部一徳', {u'birth': unicode(datetime.datetime(1947, 1, 9))})
	update(u'沢田研二', {u'birth': unicode(datetime.datetime(1948, 6, 25))})
	update(u'加橋かつみ', {u'birth': unicode(datetime.datetime(1948, 2, 4))})
	update(u'森本太郎', {u'birth': unicode(datetime.datetime(1946, 11, 18))})
	update(u'瞳みのる', {u'birth': unicode(datetime.datetime(1946, 9, 22))})

_main()

