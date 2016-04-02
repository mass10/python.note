#!/usr/bin/env python
# coding: utf-8

import riak
import uuid
import urllib2

def _insert(bucket, user_name):

	# new_id = unicode(uuid.uuid4())
	new_id = urllib2.quote(user_name.encode('utf-8'))
	new_entry = {
		u'user_name': user_name
	}
	bucket.new(new_id, new_entry).store()

def _main():

	server = riak.RiakClient(pb_port = 8087)
	bucket = server.bucket(u'The Tigers')
	create = lambda user_name: _insert(bucket, user_name)
	create(u'岸部シロー')
	create(u'岸部一徳')
	create(u'沢田研二')
	create(u'加橋かつみ')
	create(u'森本太郎')
	create(u'瞳みのる')

_main()

