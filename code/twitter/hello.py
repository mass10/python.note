#!/usr/bin/env python3
# coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import yaml
import pathlib

def configure():
	path = "{}/.twitter-settings.yml".format(pathlib.Path.home())
	file = open(path)
	conf = yaml.load(file)
	file.close()
	return conf

def tweet_hello():
	settings = configure()
	twitter = OAuth1Session(settings['consumer_key'], settings['consumer_secret'], settings['token'], settings['token_secret'])
	params = {"status": "hello #test"}
	req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)
	print(req)

def main():

	tweet_hello()

main()
