#!/usr/bin/env python
# coding: utf-8

import os
import sys
import subprocess


def _println(*arguments):

	for x in arguments:
		sys.stdout.write(str(x))
	sys.stdout.write("\n")

def _test1():

	_println('$$$ test1 $$$')

	command_text = '/bin/ls -lF /tmp/'
	
	# 'file object'
	stream = subprocess.Popen(
		command_text,
		shell=True,
		# bufsize=4096,
		stderr=subprocess.STDOUT,
		stdout=subprocess.PIPE).stdout
	for line in stream:
		_println('[', line.strip(), ']')
	stream.close()

def _test2():

	_println('$$$ test2 $$$')

	# 'file object'
	stream = os.popen('ls -lF /tmp')
	for line in stream:
		_println('[', line.strip(), ']')
	stream.close()

def main():

	_println('### start ###')

	_test1()

	_test2()

	_println('--- end ---')

main()

