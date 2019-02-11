#!/usr/bin/env python3

import MeCab

def main():

	mecab = MeCab.Tagger("-Ochasen")
	print(mecab.parse("庭には二羽、鶏がいます。"))

main()
