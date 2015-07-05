#!/usr/bin/env python
# coding: utf-8

import json

def _main():

	file = open('example.json')
	content = json.load(file)
	file.close()

	print json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4)

_main()




