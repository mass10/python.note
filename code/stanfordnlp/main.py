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

	stanfordnlp.download("ja")
	nlp = stanfordnlp.Pipeline(lang="ja")
	doc = nlp("にわにはにわにわとりがいます")

	# shows
	# ('に', '7', 'advmod')
	# ('わには', '7', 'advmod')
	# ('に', '2', 'case')
	# ('わに', '5', 'compound')
	# ('わとり', '7', 'nsubj')
	# ('が', '5', 'case')
	# ('い', '0', 'root')
	# ('ます', '7', 'aux')
	doc.sentences[0].print_dependencies()

def test_japanese2():

	stanfordnlp.download("ja")
	nlp = stanfordnlp.Pipeline(lang="ja")
	doc = nlp("庭には二羽鶏がいます。")

	# shows
	# ('庭', '7', 'iobj')
	# ('に', '1', 'case')
	# ('は', '1', 'case')
	# ('二', '5', 'nummod')
	# ('羽鶏', '7', 'nsubj')
	# ('が', '5', 'case')
	# ('い', '0', 'root')
	# ('ます', '7', 'aux')
	# ('。', '7', 'punct')
	doc.sentences[0].print_dependencies()

def main():

	test_english()
	test_japanese()
	test_japanese2()

main()
