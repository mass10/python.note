#!/usr/bin/env python3
# coding: utf-8

import os
import argparse
import PIL.Image

RATE = 0.94

def load_image(path):
	return PIL.Image.open(path)

def filter_size(width, height):
	return width * RATE, height * RATE

def new_size(width, height):
	if width > height:
		# landscape
		rate = 1920.0 / width
		return 1920.0, height * rate
	else:
		# portrait
		rate = 1080.0 / height
		return width * rate, 1080.0

def resize_to_desktop(path):
	image = load_image(path)
	width, height = new_size(image.width, image.height)
	if width == image.width:
		print("[info] nothing to do {}.".format(path))
		return
	if height == image.height:
		print("[info] nothing to do {}.".format(path))
		return
	print("[info] detect {}.".format(path))
	width, height = filter_size(width, height)
	image = image.resize((int(width), int(height)), PIL.Image.LANCZOS)
	image.save(path)

def enumerate_entries(path, handler):
	if os.path.isdir(path):
		for x in os.listdir(path):
			enumerate_entries(os.path.join(path, x), handler)
	elif os.path.exists(path):
		handler(path)
	else:
		print("[WARN] unknown path [{}].".format(path))

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--image-file",
		dest = "image_path",
		help = "Path to the The image you\"d like to resize (to desktop size).")
	args = parser.parse_args()
	if args.image_path == None or args.image_path == "":
		print("{}".format(parser.print_help()))
		return
	enumerate_entries(args.image_path, resize_to_desktop)

main()
