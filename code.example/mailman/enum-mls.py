#!/usr/bin/python
# coding: utf-8

import sys
sys.path.append('/usr/lib64/python2.6/site-packages')
sys.path.append('/usr/lib/mailman')
import getopt
import time
import datetime
import Mailman.MailList
import Mailman.mm_cfg
import Mailman.Utils
import Mailman.Errors
import optparse











###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class out:

	@staticmethod
	def println(*arguments):

		xwrite = sys.stdout.write
		for x in arguments:
			xwrite(str(x))
		xwrite("\n")






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class util:

	@staticmethod
	def timestamp():

		x = datetime.datetime.now();
		return x.isoformat(' ');

	@staticmethod
	def timelong_to_string(x):

		xx = datetime.datetime.fromtimestamp(x)
		return xx.isoformat(' ')

	@staticmethod
	def straighten(x):

		return x.replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class main:

	# =====================================================================
	# 属性のセットアップ
	# =====================================================================
	ATTRIBUTES = []
	# 説明文
	ATTRIBUTES.append('description')
	# メーリングリスト作成日時
	ATTRIBUTES.append('created_at')
	# 最終ポスト日時
	ATTRIBUTES.append('last_post_time')
	# 投稿許可者機能
	ATTRIBUTES.append('generic_nonmember_action')
	# 推奨言語
	ATTRIBUTES.append('preferred_language')
	# 退会閾値
	ATTRIBUTES.append('bounce_score_threshold')
	# 最終ポストID(=番号)
	ATTRIBUTES.append('post_id')
	# 件名の書式
	ATTRIBUTES.append('subject_prefix')
	# ?
	ATTRIBUTES.append('bounce_notify_owner_on_disable')
	# ?
	ATTRIBUTES.append('bounce_notify_owner_on_removal')
	# ?
	ATTRIBUTES.append('bounce_processing')
	# ?
	ATTRIBUTES.append('bounce_info_stale_after')
	# ?
	ATTRIBUTES.append('bounce_you_are_disabled_warnings')
	# ?
	ATTRIBUTES.append('bounce_you_are_disabled_warnings_interval')
	# メーリングリスト管理者
	ATTRIBUTES.append('owner')
	# 投稿許可者リスト
	ATTRIBUTES.append('accept_these_nonmembers')
	# メーリングリストメンバー
	ATTRIBUTES.append('members')
	ATTRIBUTES.sort()

	@staticmethod
	def _show_time_value(name, value):
	
		out.println('    ', name, ': [', value, '] (', util.timelong_to_string(value), ')')

	@staticmethod
	def _dump_attribute(mlist, name):

		value = getattr(mlist, name)
		if name == 'description':
			# 説明文
			value = value.decode('euc-jp').encode('utf-8')
			value = util.straighten(value)
			out.println('    ', name, ': [', value, ']')
		elif name == 'created_at':
			# メーリングリスト作成日時
			main._show_time_value(name, value)
		elif name == 'last_post_time':
			# 最終ポスト日時
			main._show_time_value(name, value)
		elif name == 'owner':
			# メーリングリストオーナーの出力
			out.println('    ', name, ':')
			for owner in value:
				out.println('        [', owner, ']')
			if len(value) == 0:
				out.println('        (none)')
		elif name == 'members':
			# メンバー情報の出力(ディクショナリオブジェクト)
			out.println('    ', name, ':');
			# 出力
			bounce_info_count = 0
			for member in sorted(value.keys()):
				out.println('        [', member, '] [', mlist.members[member], ']')
				# 不達状況
				bounce_info = mlist.getBounceInfo(member)
				if not bounce_info:
					continue
				out.println('            -bounce-');
				out.println('            current score: [', bounce_info.score, ']');
				out.println('            last bounce date: [', bounce_info.date, ']');
				out.println('            email notices left: [', bounce_info.noticesleft, ']')
				out.println('            last notice date: [', bounce_info.lastnotice, ']')
				out.println('            confirmation cookie: [', bounce_info.cookie, ']')
				bounce_info_count += 1
			if len(value) == 0:
				out.println('        (none)')
			if bounce_info_count == 0:
				out.println('        ※bounce に関する情報はありません。')
		elif name == 'accept_these_nonmembers':
			# 投稿許可者
			out.println('    ', name, ':')
			for member in value:
				out.println('        [', member, ']')
			if len(value) == 0:
				out.println('        (none)')
		else:
			# 単純な値の出力
			out.println('    ', name, ': [', value, ']')

	# メーリングリスト情報のダンプ
	@staticmethod
	def _dump_mlist(mlist):

		# 出力
		out.println('---')
		out.println('list_address: [', mlist.list_address, ']')
		for x in main.ATTRIBUTES:
			main._dump_attribute(mlist, x)
		out.println()

	# メーリングリスト情報のダンプ
	@staticmethod
	def _print_list_data(list_name):

		# 検索
		mlist = Mailman.MailList.MailList(list_name, lock=0)
		# ダンプ
		main._dump_mlist(mlist)
		# 開放
		if mlist.Locked():
			out.println('(unlocking)')
			mlist.Unlock()
			out.println('(unlocked)')

	@staticmethod
	def _print_system_configuration():

		out.println('#')	
		out.println('# SYSTEM CONFIGURATION')	
		out.println('#')
	
		names = []
		names.append('DEFAULT_BOUNCE_PROCESSING')
		names.append('DEFAULT_BOUNCE_SCORE_THRESHOLD')
		names.append('DEFAULT_BOUNCE_INFO_STALE_AFTER')
		names.append('DEFAULT_BOUNCE_YOU_ARE_DISABLED_WARNINGS')
		names.append('DEFAULT_BOUNCE_YOU_ARE_DISABLED_WARNINGS_INTERVAL')
		names.append('DEFAULT_BOUNCE_NOTIFY_OWNER_ON_DISABLE')
		names.append('DEFAULT_BOUNCE_NOTIFY_OWNER_ON_REMOVAL')
		names.append('REGISTER_BOUNCES_EVERY')
		names.sort()
	
		# システム情報のダンプ
		conf = Mailman.mm_cfg
		for name in names:
			out.println(name, '=[', getattr(conf, name), ']')
		out.println()

	@staticmethod
	def _show_mailinglists(options):

		out.println('#')
		out.println('# MAILING LISTS')
		out.println('#')

		# =====================================================================
		# メーリングリスト名の抽出と絞込み
		# =====================================================================
		names = []

		for list_name in sorted(Mailman.Utils.list_names()):
			# フィルタ文字列でリスト名をフィルタします。
			if options.filter != None:
				if not list_name.count(options.filter):
					continue
			names.append(list_name)

		# =====================================================================
		# 出力
		# =====================================================================
		found = 0

		for list_name in names:
			# 名前が部分的に一致した ML を表示
			main._print_list_data(list_name);
			found += 1

		if found == 0:
			out.println('no MLs found')

	@staticmethod
	def _main(argv):

		# =====================================================================
		# setup
		# =====================================================================
		p = optparse.OptionParser()
		p.add_option('--filter', dest='filter')
		(options, args) = p.parse_args()
		
		# =====================================================================
		# show system configuration
		# =====================================================================
		main._print_system_configuration()

		# =====================================================================
		# print
		# =====================================================================
		main._show_mailinglists(options)

#
# startup
#
main._main(sys.argv)
