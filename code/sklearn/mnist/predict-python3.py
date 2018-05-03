#!/usr/bin/env python3
# coding: utf-8

import sys
from sklearn import datasets, svm, metrics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import numpy
from PIL import Image

def _load_image(image_path):

	image = Image.open(image_path).convert("L")
	image = image.resize((8, 8), Image.ANTIALIAS)
	img = numpy.asarray(image, dtype=float)
	img = numpy.floor(16 - 16 * (img / 256))

	# 識別用に粗く変換した状態の画像
	if True:
		matplotlib.pyplot.imshow(img)
		matplotlib.pyplot.gray()
		matplotlib.pyplot.show()
		matplotlib.pyplot.savefig("識別用に変換された画像.png")

	img = img.flatten()
	print("[trace] img:", img)
	return img

def _predict(sample_image):

	# 手書き数字データをダウンロードしています。
	digits = datasets.load_digits()
	# 分類器(C-Support Vector Classification)
	classifier = svm.SVC(gamma=0.001)
	# 学習
	classifier.fit(digits.data, digits.target)
	# サンプル画像を分類します。
	predicted = classifier.predict([sample_image])
	print(predicted)

def _main(argv):

	if len(argv) == 1:
		print("path to image?")
		return
	# 画像を読み込みます。
	sample_image = _load_image(argv[1])
	# 分類します。
	_predict(sample_image)

_main(sys.argv)
