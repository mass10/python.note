#!/usr/bin/env python
# coding: utf-8

import os
import sys
import argparse
import base64
import httplib2
import json
import pprint 
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import logging

def load_image_from_file(path):

	with open(path, 'rb') as image:
		return base64.b64encode(image.read())

def main(photo_file):

	if photo_file == None or photo_file == '':
		print 'No file'
		return

	os.environ[u'GOOGLE_APPLICATION_CREDENTIALS'] = u'/home/ec2-user/.google/vision-api-no-test-d7262692285e.json'

	logging.raiseExceptions = True #True: Debugging, False: Production
	logging.basicConfig(stream = sys.stdout, level = logging.DEBUG)

	# =========================================================================
	# 認証
	# =========================================================================

	credentials = GoogleCredentials.get_application_default()

	# http = httplib2.Http()
	# credentials = GoogleCredentials.get_application_default().create_scoped(
	# 	[
	# 		'https://www.googleapis.com/auth/cloud-platform',
	# 	]
	# )
	# credentials.authorize(http)

	# =========================================================================
	# リクエスト
	# =========================================================================
	API_DISCOVERY_FILE = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
	service = discovery.build('vision', 'v1', credentials=credentials, discoveryServiceUrl = API_DISCOVERY_FILE)
	image_content = load_image_from_file(photo_file)
	body = {
		'requests': [
			{
				'image': {
					'content': image_content.decode('UTF-8')
				},
				'features': [
					{
						'type': 'TEXT_DETECTION',
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
	json_text = json.dumps(response, indent = 4, ensure_ascii = False, encoding = 'utf-8')
	print json_text.encode('utf-8')

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--image-file', help = 'The image you\'d like to label.')
	args = parser.parse_args()
	main(args.image_file)
