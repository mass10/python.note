#!/usr/bin/env python3

import nltk

def _main():
	# ステミング
	stemmer = nltk.PorterStemmer()
	print(stemmer.stem("Running"))
	print(stemmer.stem("Daniel"))
	print(stemmer.stem("CLUSTERING"))
	print(stemmer.stem("cluster"))
	print(stemmer.stem("clustered"))
	print(stemmer.stem("Speaker"))
	print(stemmer.stem("Speech"))
	print(stemmer.stem("speaking"))
	print(stemmer.stem("spoken"))

_main()
