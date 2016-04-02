#!/usr/bin/env python
# coding: utf-8

import riak
import uuid
import datetime
import urllib2

def _update(bucket, user_name, name, value):

	key = urllib2.quote(user_name.encode('utf-8'))
	e = bucket.get(key)
	if e == None:
		return
	e.data[name] = value
	e.store()

def _main():

	server = riak.RiakClient(pb_port = 8087)
	bucket = server.bucket(u'The Tigers')
	update = lambda user_name, location: _update(bucket, user_name, u'birthplace', location)
	update(u'岸部シロー', u'京都府京都市')
	update(u'岸部一徳', u'京都府京都市')
	update(u'沢田研二', u'鳥取県鳥取市')
	update(u'加橋かつみ', u'大阪府堺市')
	update(u'森本太郎', u'京都府京都市')
	update(u'瞳みのる', u'京都府')

_main()

