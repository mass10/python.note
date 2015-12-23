#!/usr/bin/env python
# coding: utf-8

# import os
# import codecs
import io


def _main():

	file = io.open('sample.txt', mode='w', encoding='utf-8')
	file.write(u'こんにちは')
	file.write(u"\n")
	file.write(u'こんにちは')
	file.write(u"\n")
	file.write(u'こんにちは')
	file.write(u"\n")
	file.close()

	# file = os.open('sample.txt', 0644)
	# writer = codecs.getwriter('utf-8')(file)
	# writer.writeline('列1	列2	列3')
	# writer.writeline('VALUE-01	VALUE-02	VALUE-03', "\n")
	# file.close()

_main()
