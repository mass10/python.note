#!/usr/bin/env python
# coding: utf-8

import urllib

def _main():

	print '単純なURLエンコーディングの例'
	print urllib.quote('ああああああああああああああ')

	print ''
	print 'dict からクエリーストリングを生成する例'
	print urllib.urlencode(
		{
			'id': '801f66a9-6325-4f72-a699-fe57213c80a6',
			'referer': 'https://ja.wikipedia.org/wiki/%E3%81%82%E3%81%84%E3%81%8A%E5%B8%82',
			'selected-item': 'あいお市',
		}
	)

_main()

