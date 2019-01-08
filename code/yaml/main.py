#!/usr/bin/env python3
# coding: utf-8

import yaml
import json

def main():

	file = open("settings.yml", "r")
	conf = yaml.load(file)
	conf = json.dumps(conf, indent=4)
	print(conf)
	file.close()

main()

