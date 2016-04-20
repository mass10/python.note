#!/usr/bin/env python
# coding: utf-8

import uuid

def main():

	# network address を含むため、プライバシーを漏らす。
	print uuid.uuid1()

	# ランダムな文字列を生成する。
	print uuid.uuid4()

main()
