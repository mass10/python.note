import datetime

def get_current_timestamp():

	now = datetime.datetime.now()
	return "{0:%Y-%m-%d %H:%M:%S.%f}".format(now)

def application(env, start_response):

	start_response('202 OK', [('Content-Type','text/html')])

	timestamp = get_current_timestamp()

	response = """
<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		{0}: いきてます!
	</body>
</html>
	""".format(timestamp)

	return response.encode('utf-8')
