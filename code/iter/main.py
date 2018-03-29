#!/usr/bin/env python3
# coding: utf-8

class hard_map:

	def __init__(self):
		self.__set = {}

	# インデクサによる参照要求
	def __getitem__(self, key):
		return self.__set.get(key)

	# インデクサによる書き込み要求
	def __setitem__(self, key, value):
		# 既にキーが存在する場合は書き換えを拒否します。
		if key in self.__set:
			return False
		self.__set[key] = value
		return True

	# in の提供
	def __contains__(self, key):
		return key in self.__set

	# for によるイテレーションの提供
	def __iter__(self):
		self.__iter = iter(self.__set)
		return self.__iter

	def __next__(self):
		return next(self.__iter)

def _main():

	m = hard_map()

	# "hokkaido" という新しいキーで "北海道" を登録
	m["hokkaido"] = "北海道"
	# 書き換えできない(無視)
	m["hokkaido"] = "北海道2"

	# "aomori" という新しいキーで "青森" を登録
	m["aomori"] = "青森"
	# 書き換えできない(無視)
	m["aomori"] = "青森2"

	# "okinawa" という新しいキーで "沖縄" を登録
	m["okinawa"] = "沖縄"

	# False
	print("yamagata" in m)
	# True
	print("okinawa" in m)

	# m の内容を表示
	for e in m:
		print("{}: {}".format(e, m[e]))

_main()
