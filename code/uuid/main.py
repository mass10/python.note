#!/usr/bin/env python3
# coding: utf-8

import uuid

def main():

	# network address に依存する情報を含んでおり、プライバシーを漏らす。
	print(uuid.uuid1())

	# ランダムな文字列を生成する。
	print(uuid.uuid4())

main()
