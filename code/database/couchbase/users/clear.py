#!/usr/bin/env python
# coding: utf-8

from couchbase.bucket import *

def _main():

	b = Bucket('couchbase://127.0.0.1/USERS')
	b.flush()

_main()

