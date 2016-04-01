#!/usr/bin/env python
# coding: utf-8

import riak
import uuid
import urllib2

def _insert(bucket, user_name, birthplace):

	new_id = unicode(uuid.uuid4())
	new_id = urllib2.quote(user_name.encode('utf-8'))
	new_entry = {
		u'user_name': user_name,
		u'birthplace': birthplace
	}
	bucket.new(new_id, new_entry).store()

def _main():

	server = riak.RiakClient(pb_port=8087)
	bucket = server.bucket(u'The Tigers')
	create_member = lambda user_name, birthplace: _insert(bucket, user_name, birthplace)
	create_member(u'岸部シロー', u'京都府京都市')
	create_member(u'岸部一徳', u'京都府京都市')
	create_member(u'沢田研二', u'鳥取県鳥取市')
	create_member(u'加橋かつみ', u'大阪府堺市')
	create_member(u'森本太郎', u'京都府京都市')
	create_member(u'瞳みのる', u'京都府')

_main()

