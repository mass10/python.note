#!/usr/bin/env python
# coding: utf-8
#
#
# Slack の Incoming Webhook を利用して、特定の channel にメッセージを飛ばす例
#
#
#

import io
import requests
import json

def _get_webhook_url():

	file = io.open('.slack-webhook.url')
	url = file.readline()
	url = url.rstrip()
	file.close()
	return url

def _main():

	fields = {
		# 'channel': '不要(設定済みのチャネルに飛ぶ)',
		# 'username': '不要(設定済みのユーザー名が適用される)', 
		'text': 'テスト',
		# 'icon_emoji': ':ghost:',
	}

	content = json.dumps(fields, ensure_ascii=False)

	url = _get_webhook_url()
	response = requests.post(url, data=content)
	print(response.text)

_main()
