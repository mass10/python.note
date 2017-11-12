#!/usr/bin/env python3
# coding: utf-8
#
# property のサンプル
#
#



class person(object):

	def __init__(self):
		self.__name = ''
	def getname(self):
		return self.__name
	def setname(self, name):
		self.__name = name
	name = property(getname, setname)

def main():

	i = person()
	print('initial name: [{}]'.format(i.name))

	i.name = 'だいだらぼっち'
	print('modified name: [{}]'.format(i.name))

	i.setname('ろくろくび')
	print('modified name: [{}]'.format(i.getname()))

main()

