#!/usr/bin/env python
# coding: utf-8

import argparse


def _main():

	parser = argparse.ArgumentParser()

	parser.add_argument(
		'--image-file',
		dest = 'image_path',
		help = 'Path to the The image you\'d like to post.')

	parser.add_argument(
		'--verbose',
		dest = 'verbose',
		action = 'count',
		help = 'It will be a little verbose.')

	args = parser.parse_args()

	if args.image_path == None or args.image_path == "":
		print parser.print_help()
		return

	print('image_path: [{}]'.format(args.image_path))
	print('verbose: [{}]'.format(args.verbose))

_main()

