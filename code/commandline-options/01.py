#!/usr/bin/python
# coding: utf-8

import sys
import optparse



def _main(argv):

	p = optparse.OptionParser(usage=u'使用方法')

	p.add_option('--v',
		action='store_true',
		default=False,
		dest='v',
		help=u'冗長モードで実行します。')
	p.add_option('--vv',
		action='store_true',
		default=False,
		dest='vv',
		help=u'冗長モードで実行します。')
	p.add_option('--vvv',
		action='store_true',
		default=False,
		dest='vvv',
		help=u'冗長モードで実行します。')
	p.add_option('--function',
		default=None,
		dest='function',
		help=u'機能IDを指定してください。')

	(options, args) = p.parse_args()

	if options.function is None or options.function == '':
		p.print_help()
		return

	print('v=[{}]'.format(options.v))
	print('vv=[{}]'.format(options.vv))
	print('vvv=[{}]'.format(options.vvv))
	print('function=[{}]'.format(options.function))

_main(sys.argv)
