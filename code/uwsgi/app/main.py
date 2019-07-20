def application(env, start_response):

	start_response('202 OK', [('Content-Type','text/html')])

	response = """
<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		いきてます!
	</body>
</html>
	"""
	return response.encode('utf-8')
