#!//usr/bin/env python
# coding: utf-8


import json
import urllib2
import flask
import datetime

from couchbase import *
from couchbase.bucket import *
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():

	content_text = '''
	<html>
	<body>
	Hello Flask World!
	</body>
	</html>
	'''
	return content_text

@app.route('/users')
def users():

	users = []

	bucket = Bucket('couchbase://127.0.0.1/USERS')
	result = bucket.query('users', 'V_USERS_02',
		use_devmode = False, limit = 99999, skip = 0)
	for e in result:
		user_data = json.dumps(e.value,
			ensure_ascii = False, sort_keys = True, encoding = 'utf-8')
		users.append(user_data)

	fields = {
		u'timestamp': datetime.datetime.now(),
		u'users': users
	}

	return render_template('users.html', fields=fields)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0')
