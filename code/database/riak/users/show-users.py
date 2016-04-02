#!/usr/bin/env python
# coding: utf-8

import riak
import json
import urllib2
import pprint

def _main():

	server = riak.RiakClient(pb_port=8087)
	bucket = server.bucket(u'The Tigers')

	for key in bucket.get_keys():
		e = bucket.get(key)
		data = e.data
		# key = urllib2.unquote(key)
		# key = key.decode('utf-8')
		data = {u'key': key, u'data': data, u'etag': e.etag}
		print json.dumps(data, ensure_ascii = False, sort_keys = True, indent = 2)

_main()

