#!/usr/bin/env python3
# coding: utf-8

import stanfordnlp

def test_english():

	stanfordnlp.download('en')
	nlp = stanfordnlp.Pipeline()
	doc = nlp("I like small owls.")

	# shows
	# ('I', '2', 'nsubj')
	# ('like', '0', 'root')
	# ('small', '4', 'amod')
	# ('owls', '2', 'obj')
	# ('.', '2', 'punct')
	doc.sentences[0].print_dependencies()

def test_japanese():

	stanfordnlp.download('ja')
	nlp = stanfordnlp.Pipeline()
	doc = nlp("にわにはにわにわとりがいます")

	# shows
	# ('にわにはにわにわとりがいます', '0', 'root')
	doc.sentences[0].print_dependencies()

def test_japanese2():

	stanfordnlp.download('ja')
	nlp = stanfordnlp.Pipeline()
	doc = nlp("庭には二羽鶏がいます。")

	# shows
	# ('庭には二羽鶏がいます。', '0', 'root')
	doc.sentences[0].print_dependencies()

def main():

	test_english()
	test_japanese()
	test_japanese2()

main()
