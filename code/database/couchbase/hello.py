#!/usr/bin/env python
# coding: utf-8

from couchbase import *
from couchbase.bucket import *

def _main():

	b = Bucket('couchbase://127.0.0.1/beer-sample')

	for e in b.query('name', '563 Stout', limit=-1):
		print e

	print b.get('21st_amendment_brewery_cafe-563_stout')
	print b.get('aass_brewery-juleol')

_main()

