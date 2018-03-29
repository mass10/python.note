#!/usr/bin/env python3
# coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import sys
import yaml
import pathlib
import io

def configure():
	path = "{}/.twitter-settings.yml".format(pathlib.Path.home())
	with open(path) as f:
		conf = yaml.load(f)
		return conf

def tweet(text):
	if text == "":
		print("canceled.")
		return
	print("text: [", text, "]", sep="")
	conf = configure()
	twitter = OAuth1Session(
		conf["consumer_key"],
		conf["consumer_secret"],
		conf["token"],
		conf["token_secret"])
	params = {"status": text}
	req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)
	print("RESPONSE:", req, sep="")

def read_text():
	s = io.StringIO()
	reader = sys.stdin
	for line in reader:
		if line == ".\n":
			break
		if line == ".\r\n":
			break
		s.write(line)
	return s.getvalue().rstrip()

def main():
	text = read_text()
	tweet(text)

main()
