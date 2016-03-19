#!/usr/bin/env python
# coding: utf-8

import sys
import codecs
import json

def _println(*args):
	out = codecs.getwriter('utf-8')(sys.stdout)
	for x in args:
		out.write(x)
	out.write(u"\n")

def _main():

	for i in (range(0, 9)):

		j = {
			u"id": unicode(i),
			u"email": u"test-{}@example.jp".format(i),
			u"name": u"{} さん".format(i),
			u"address": u"東京都八王子市高尾 {}".format(i),
		}

		json_text = json.dumps(j, ensure_ascii = False, sort_keys = False)

		_println(json_text)

_main()
