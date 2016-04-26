#!/usr/bin/env python
# coding: utf-8


import argparse
import base64
import httplib2
import json
import pprint 
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
from PIL import Image
from PIL import ImageDraw

def highlight_faces(image, faces, output_filename):
	im = Image.open(image)
	draw = ImageDraw.Draw(im)
	for face in faces:
		box = [(v.get('x', 0.0), v.get('y', 0.0)) for v in face['fdBoundingPoly']['vertices']]
		draw.line(box + [box[0]], width=5, fill='#00ff00')
	del draw
	im.save(output_filename)

def _detect_faces(photo_file):

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
							'type': 'FACE_DETECTION',
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

	if not response.has_key('responses'):
		print 'no results.'
		return None
	if len(response['responses']) < 1:
		print 'no results.'
		return None
	if not response['responses'][0].has_key('faceAnnotations'):
		print 'no results.'
		return None
	return response['responses'][0]['faceAnnotations']

def main(path):

	# 顔認識
	faces = _detect_faces(path)
	if faces is None:
		return
	# 名前を付けてファイルを保存
	with open(path, 'rb') as image:
		highlight_faces(image, faces, 'out.jpg')

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--image-file', help = 'The image you\'d like to label.')
	args = parser.parse_args()
	main(args.image_file)
