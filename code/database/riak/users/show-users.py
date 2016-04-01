#!/usr/bin/env python
# coding: utf-8

import riak
import json
import urllib2

def _main():

	server = riak.RiakClient(pb_port=8087)
	bucket = server.bucket(u'The Tigers')

	for key in bucket.get_keys():
		e = bucket.get(key)
		text = e.data
		# key = urllib2.unquote(key)
		# key = key.decode('utf-8')
		print json.dumps({u'key': key, u'data': text}, ensure_ascii = False, sort_keys = True)

_main()

