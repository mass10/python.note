#!/usr/bin/env python
# coding: utf-8


def _main():

	print u'### BEGIN ###'

	try:
		# Raises with Python 2.6.6
		open('', 'r')
	except IOError as e:
		print u'[ERROR]', unicode(e)
	finally:
		print u'done.'

	try:
		# Raises with Python 2.6.6
		str(u'あ')
	except UnicodeEncodeError as e:
		print u'[ERROR]', e
	finally:
		print u'done.'

	try:
		# Raises with Python 2.6.6
		raise Exception(u'例外のテスト')
	except Exception as e:
		print u'[ERROR]', unicode(e)
	finally:
		print u'done.'

	try:
		# Raises with Python 2.6.6
		999 / 0
	except ZeroDivisionError as e:
		print u'[ERROR]', unicode(e)
	# except Exception as e:
	# 	print(unicode(e))
	else:
		print u'else'
	finally:
		print u'done.'

	try:
		# Raises with Python 2.6.6
		raise Exception(u'例外のテスト')
	except Exception as e:
		print '[ERROR]', unicode(e)
	finally:
		print u'done.'

	print u'--- END ---'

_main()

