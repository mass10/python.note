#!/usr/bin/env python
# coding: utf-8


import sys
import os
import ldap3
import datetime
import time
import codecs



##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
class constants:

	HOST = '192.168.141.129';
	PORT = 389;
	PRINCIPAL = 'cn=Manager,dc=example,dc=jp';
	PASSWORD = 'root';






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class out:

	@staticmethod
	def println(*arguments):

		out = codecs.getwriter('utf-8')(sys.stdout)
		for x in arguments:
			out.write('' + x)
		out.write("\n")






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class util:

	# "yyyy-mm-dd hh:mm:ss.xxxxxx"
	@staticmethod
	def timestamp():

		x = datetime.datetime.now();
		return x.isoformat(' ');






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class stopwatch:

	_value = None

	def __init__(self):

		self._member = datetime.datetime.now()

	def __repr__(self):

		current = datetime.datetime.now()
		elapsed = current - self._member
		return str(elapsed)






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class logger:

	@staticmethod
	def error(*arguments):

		out.println(util.timestamp(), ' [error] ', *arguments)

	@staticmethod
	def info(*arguments):

		out.println(util.timestamp(), ' [info] ', *arguments)

	@staticmethod
	def debug(*arguments):

		out.println(util.timestamp(), ' [debug] ', *arguments)






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class main:

	@staticmethod
	def _create_tree():

		# LDAP サーバーに接続します。
		server_info = ldap3.Server(
				constants.HOST,
				constants.PORT)
		session = ldap3.Connection(
				server_info,
				auto_bind = True,
				client_strategy = ldap3.STRATEGY_SYNC,
				user = constants.PRINCIPAL,
				password = constants.PASSWORD,
				raise_exceptions = True)
		try:
			# ROOT ノードを作成します。
			response = session.add(
					'dc=example,dc=jp',
					object_class = ['dcObject', 'organization'],
					attributes = {'dc': 'example', 'o': 'myorganization'})
			# グループ用のノードを作成します。
			response = session.add(
					'ou=People,dc=example,dc=jp',
					object_class = ['organizationalUnit'],
					attributes = {'ou': 'People'})
			# アカウントを作成します。
			response = session.add(
					'uid=user.000,ou=People,dc=example,dc=jp',
					object_class = ['top', 'inetOrgPerson'],
					attributes = {'uid': 'user.000', 'sn': 'user.000', 'cn': 'user.000', 'mail': 'user.000@example.jp'})
			response = session.add(
					'uid=user.001,ou=People,dc=example,dc=jp',
					object_class = ['top', 'inetOrgPerson'],
					attributes = {'uid': 'user.001', 'sn': 'user.001', 'cn': 'user.001', 'mail': 'user.001@example.jp'})
			response = session.add(
					'uid=user.002,ou=People,dc=example,dc=jp',
					object_class = ['top', 'inetOrgPerson'],
					attributes = {'uid': 'user.002', 'sn': 'user.002', 'cn': 'user.002', 'mail': 'user.002@example.jp'})
		except Exception as e:
			logger.error(str(e))
		session.unbind()

	@staticmethod
	def main():

		watch = stopwatch()
		logger.info('### start ###')
		main._create_tree()
		logger.info(u'処理時間=[', str(watch), ']')
		logger.info('--- end ---')

main.main();
