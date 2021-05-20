#!/usr/bin/env python3
# coding: utf-8

from PIL import Image, ImageFilter

def _convert_image_as_png(path_left, path_right):

	image = Image.open(path_left)
	width = int(image.width * 0.15)
	height = int(image.height * 0.15)
	image = image.resize((width, height), Image.LANCZOS)
	image.save(path_right)

def main():

	_convert_image_as_png("IMG_3049.JPG", "IMG_3049.png")
	_convert_image_as_png("IMG_3050.JPG", "IMG_3050.png")
	_convert_image_as_png("IMG_3051.JPG", "IMG_3051.png")
	_convert_image_as_png("IMG_3052.JPG", "IMG_3052.png")
	_convert_image_as_png("IMG_3053.JPG", "IMG_3053.png")
	_convert_image_as_png("IMG_3054.JPG", "IMG_3054.png")
	_convert_image_as_png("IMG_3055.JPG", "IMG_3055.png")
	_convert_image_as_png("IMG_3056.JPG", "IMG_3056.png")
	_convert_image_as_png("IMG_3057.JPG", "IMG_3057.png")
	_convert_image_as_png("IMG_3058.JPG", "IMG_3058.png")
	_convert_image_as_png("IMG_3059.JPG", "IMG_3059.png")
	_convert_image_as_png("IMG_3060.JPG", "IMG_3060.png")
	_convert_image_as_png("IMG_3061.JPG", "IMG_3061.png")
	_convert_image_as_png("IMG_3062.JPG", "IMG_3062.png")
	_convert_image_as_png("IMG_3063.JPG", "IMG_3063.png")
	_convert_image_as_png("IMG_3064.JPG", "IMG_3064.png")
	_convert_image_as_png("IMG_3065.JPG", "IMG_3065.png")
	_convert_image_as_png("IMG_3066.JPG", "IMG_3066.png")
	_convert_image_as_png("IMG_3067.JPG", "IMG_3067.png")
	_convert_image_as_png("IMG_3068.JPG", "IMG_3068.png")
	_convert_image_as_png("IMG_3069.JPG", "IMG_3069.png")

main()

