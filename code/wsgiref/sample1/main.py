#!/usr/bin/env python3
# coding: utf-8

from wsgiref import simple_server

def application(environ, start_response):

	start_response('200 OK', [('Content-type', 'text/plain')])

	response = """
<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		こんにちは！
	</body>
</html>
"""
	response = response.encode("utf-8")
	return [response]

if __name__ == '__main__':
	server = simple_server.make_server('', 8080, application)
	server.serve_forever()
