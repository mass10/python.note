#!/usr/bin/env python
# coding: utf-8

import os
import sys
import riak

def _main():

	myClient = riak.RiakClient(pb_port=8087)
	myBucket = myClient.bucket('test')

	val1 = 1
	key1 = myBucket.new('one', data=val1)
	key1.store()

	val2 = "two"
	key2 = myBucket.new('two', data=val2)
	key2.store()

	val3 = {"myValue": 3}
	key3 = myBucket.new('three', data=val3)
	key3.store()

	fetched1 = myBucket.get('one')
	assert val1 == fetched1.data
	print fetched1.data

	fetched2 = myBucket.get('two')
	assert val2 == fetched2.data
	print fetched2.data

	fetched3 = myBucket.get('three')
	print fetched3.data

	print "Ok."

_main()
