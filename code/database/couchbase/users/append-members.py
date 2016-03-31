#!/usr/bin/env python
# coding: utf-8

from couchbase import *
from couchbase.bucket import *
import uuid

def _insert(bucket, user_name, birthplace):

	new_id = unicode(uuid.uuid4())
	new_entry = {
		'user_name': user_name,
		'birthplace': birthplace
	}
	bucket.insert(new_id, new_entry)

def _main():

	b = Bucket('couchbase://127.0.0.1/USERS')
	create_member = lambda user_name, birthplace: _insert(b, user_name, birthplace)
	create_member('岸部シロー', '京都府京都市')
	create_member('岸部一徳', '京都府京都市')
	create_member('沢田研二', '鳥取県鳥取市')
	create_member('加橋かつみ', '大阪府堺市')
	create_member('森本太郎', '京都府京都市')
	create_member('瞳みのる', '京都府')

_main()

