#!//usr/bin/env python
# coding: utf-8


import pymongo
import json
import urllib2
import flask
import datetime

from flask import Flask
from flask import render_template


app = Flask(__name__)

def _conversion(unknown):

	if isinstance(unknown, datetime.datetime):
		return unknown.isoformat()
	try:
		return str(unknown)
	except:
		raise TypeError(repr(unknown) + " is not JSON serializable")

@app.route("/")
def index():

	return "Hello Flask World!"

@app.route("/users")
def users():

	users = []

	client = pymongo.MongoClient('localhost', 27017, )
	db = client['test']
	collection = db['db20160325']
	for e in collection.find():
		e.pop('_id')
		user_data = json.dumps(e, ensure_ascii=False, sort_keys=False, indent=None, default=_conversion, encoding='utf-8')
		users.append(user_data)

	fields = {
		u'timestamp': datetime.datetime.now(),
		u'users': users
	}

	return render_template('users.html', fields=fields)

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0')
