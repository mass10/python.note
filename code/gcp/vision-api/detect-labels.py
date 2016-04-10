#!/usr/bin/env python
# coding: utf-8


import argparse
import base64
import httplib2
import json
import pprint 
# from apiclient.discovery import build
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials

def main(photo_file):

	# =========================================================================
	# 認証
	# =========================================================================
	http = httplib2.Http()
	credentials = GoogleCredentials.get_application_default().create_scoped(
		[
			'https://www.googleapis.com/auth/cloud-platform',
		]
	)
	credentials.authorize(http)

	# =========================================================================
	# リクエスト
	# =========================================================================
	API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
	service = build('vision', 'v1', http, discoveryServiceUrl = API_DISCOVERY_FILE)
	with open(photo_file, 'rb') as image:
		image_content = base64.b64encode(image.read())
		body = {
			'requests': [
				{
					'image': {
						'content': image_content
					},
					'features': [
						{
							'type': 'LABEL_DETECTION',
							'maxResults': 5,
						}
					]
				}
			]
		}
		service_request = service.images().annotate(body = body)

	# =========================================================================
	# 実行
	# =========================================================================
	response = service_request.execute()
	print json.dumps(response, indent = 4)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--image-file', help = 'The image you\'d like to label.')
	args = parser.parse_args()
	main(args.image_file)
