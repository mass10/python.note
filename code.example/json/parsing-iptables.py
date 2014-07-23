#!/usr/bin/env python
# coding: utf-8
#
#
# iptables の出力を json に変換します。
#
#

import sys
import subprocess
import json

def _println(*arguments):

	for x in arguments:
		sys.stdout.write(str(x))
	sys.stdout.write("\n")

def _execute():

	command = ['iptables', '--list', '-nvx', '--line-numbers']
	stream = subprocess.Popen(
			command,
			stdout=subprocess.PIPE).stdout

	current_chain = ''
	result = {}

	for line in stream:

		line = line.strip()
		if line == '':
			continue

		fields = line.split()
		if fields[0] == 'num':
			pass
		elif fields[0] == 'Chain':
			current_chain = fields[1]
			result[current_chain] = {}
		else:
			num = fields[0]
			new_entry = {
				'num': fields[0],
				'pkts': fields[1],
				'bytes': fields[2],
				'target': fields[3],
				'prot': fields[4],
				'opt': fields[5],
				'in': fields[6],
				'out': fields[7],
				'source': fields[8],
				'destination': fields[9],
			}
			result[current_chain][num] = new_entry

	stream.close()

	_println(json.dumps(result, sort_keys=True, indent=4))

def main():

	_execute()

main()




