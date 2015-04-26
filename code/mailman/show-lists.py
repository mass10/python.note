#!/usr/bin/python
# coding: utf-8

import sys
import getopt
import time
import datetime
import optparse

sys.path.append('/usr/lib/mailman')
import Mailman.MailList
import Mailman.mm_cfg
import Mailman.Utils
import Mailman.Errors











class console:

	@staticmethod
	def println(*arguments):

		xwrite = sys.stdout.write
		for x in arguments:
			xwrite(str(x))
		xwrite("\n")

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

class main:

	ATTRIBUTES = []
	ATTRIBUTES.append('description')
	ATTRIBUTES.append('created_at')
	ATTRIBUTES.append('last_post_time')
	ATTRIBUTES.append('generic_nonmember_action')
	ATTRIBUTES.append('preferred_language')
	ATTRIBUTES.append('bounce_score_threshold')
	ATTRIBUTES.append('post_id')
	ATTRIBUTES.append('subject_prefix')
	ATTRIBUTES.append('bounce_notify_owner_on_disable')
	ATTRIBUTES.append('bounce_notify_owner_on_removal')
	ATTRIBUTES.append('bounce_processing')
	ATTRIBUTES.append('bounce_info_stale_after')
	ATTRIBUTES.append('bounce_you_are_disabled_warnings')
	ATTRIBUTES.append('bounce_you_are_disabled_warnings_interval')
	ATTRIBUTES.append('owner')
	ATTRIBUTES.append('accept_these_nonmembers')
	ATTRIBUTES.append('members')
	ATTRIBUTES.sort()

	@staticmethod
	def _show_time_value(name, value):
	
		console.println('    ', name, ': [', value, '] (', util.timelong_to_string(value), ')')

	@staticmethod
	def _dump_attribute(mlist, name):

		value = getattr(mlist, name)
		if name == 'description':
			value = value.decode('euc-jp').encode('utf-8')
			value = util.straighten(value)
			console.println('    ', name, ': [', value, ']')
		elif name == 'created_at':
			main._show_time_value(name, value)
		elif name == 'last_post_time':
			main._show_time_value(name, value)
		elif name == 'owner':
			console.println('    ', name, ':')
			for owner in value:
				console.println('        [', owner, ']')
			if len(value) == 0:
				console.println('        (none)')
		elif name == 'members':
			console.println('    ', name, ':');
			bounce_info_count = 0
			for member in sorted(value.keys()):
				console.println('        [', member, '] [', mlist.members[member], ']')
				bounce_info = mlist.getBounceInfo(member)
				if not bounce_info:
					continue
				console.println('            -bounce-');
				console.println('            current score: [', bounce_info.score, ']');
				console.println('            last bounce date: [', bounce_info.date, ']');
				console.println('            email notices left: [', bounce_info.noticesleft, ']')
				console.println('            last notice date: [', bounce_info.lastnotice, ']')
				console.println('            confirmation cookie: [', bounce_info.cookie, ']')
				bounce_info_count += 1
			if len(value) == 0:
				console.println('        (none)')
			if bounce_info_count == 0:
				console.println('        ※no bounce')
		elif name == 'accept_these_nonmembers':
			console.println('    ', name, ':')
			for member in value:
				console.println('        [', member, ']')
			if len(value) == 0:
				console.println('        (none)')
		else:
			console.println('    ', name, ': [', value, ']')

	@staticmethod
	def _dump_list_information(mlist):

		console.println('---')
		console.println('list_address: [', mlist.list_address, ']')
		for x in main.ATTRIBUTES:
			main._dump_attribute(mlist, x)
		console.println()

	@staticmethod
	def _print_list_data(list_name):

		mlist = Mailman.MailList.MailList(list_name, lock=0)
		main._dump_list_information(mlist)

	@staticmethod
	def _get_attributes():

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
		return names

	@staticmethod
	def _show_system_configuration():

		console.println('#')
		console.println('# SYSTEM CONFIGURATION')
		console.println('#')
	
		conf = Mailman.mm_cfg
		names = main._get_attributes()
		for name in names:
			console.println(name, '=[', getattr(conf, name), ']')
		console.println()

	@staticmethod
	def _find_lists(filter):

		names = []
		for list_name in sorted(Mailman.Utils.list_names()):
			if options.filter is None:
				names.append(list_name)
				continue
			if list_name.count(options.filter):
				names.append(list_name)
				continue
		return names

	@staticmethod
	def _show_mailinglists(options):

		console.println('#')
		console.println('# LISTS')
		console.println('#')

		found = 0
		names = main._find_lists(options.filter)
		for list_name in names:
			main._print_list_data(list_name);
			found += 1
		if found == 0:
			console.println('no MLs found')

	@staticmethod
	def _main(argv):

		p = optparse.OptionParser()
		p.add_option('--filter', dest='filter')
		(options, args) = p.parse_args()

		main._show_system_configuration()
		main._show_mailinglists(options)

main._main(sys.argv)
