#!/usr/bin/env python3

from janome.tokenizer import Tokenizer

def main():

	t = Tokenizer()
	for token in t.tokenize("庭には二羽、鶏がいます。"):
		print(token)

main()

