#!/usr/bin/env python3
# coding: utf-8
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot
import sklearn.datasets

def main():

	digits = sklearn.datasets.load_digits()

	print("[trace] 手書きデータの数:", len(digits.data), sep="")

	# 25 個のランダムな整数
	p = numpy.random.random_integers(0, len(digits.data), 25)

	position = 0
	for n in p:
		image, label = digits.images[n], digits.target[n]
		matplotlib.pyplot.subplot(5, 5, 1 + position)
		matplotlib.pyplot.axis("off")
		# image = image.reshape((28, 28))
		matplotlib.pyplot.imshow(image, cmap=matplotlib.pyplot.cm.gray_r, interpolation='nearest')
		matplotlib.pyplot.title('Training: %i' % label)
		position = position + 1
	matplotlib.pyplot.show()
	matplotlib.pyplot.savefig("out.png")

main()

