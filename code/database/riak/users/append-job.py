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
	update(u'岸部シロー', {u'job': u'ザ・タイガース'})
	update(u'岸部一徳', {u'job': u'ザ・タイガース'})
	update(u'沢田研二', {u'job': u'ザ・タイガース'})
	update(u'加橋かつみ', {u'job': u'ザ・タイガース'})
	update(u'森本太郎', {u'job': u'ザ・タイガース'})
	update(u'瞳みのる', {u'job': u'ザ・タイガース'})

_main()

