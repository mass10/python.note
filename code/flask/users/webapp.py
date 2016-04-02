#!//usr/bin/env python
# coding: utf-8


import riak
import json
import urllib2
import flask
import datetime

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():

	content_text = """
	<html>
	<body>
	Hello Flask World!
	</body>
	</html>
	"""
	return content_text

@app.route("/users")
def users():

	users = []

	server = riak.RiakClient(pb_port = 8087)
	bucket = server.bucket(u'The Tigers')
	for key in bucket.get_keys():
		e = bucket.get(key)
		user_data = e.data
		user_data = json.dumps(user_data, ensure_ascii = False, sort_keys = True)
		users.append(user_data)

	fields = {
		u'timestamp': datetime.datetime.now(),
		u'users': users
	}

	return render_template('users.html', fields=fields)

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0')
