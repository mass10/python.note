#!/usr/bin/env python
# coding: utf-8

import riak

def _main():

	myClient = riak.RiakClient(pb_port=8087)
	myBucket = myClient.bucket(u'The Tigers')
	for key in myBucket.get_keys():
		myBucket.delete(key)

_main()

