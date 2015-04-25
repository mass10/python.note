#!/usr/bin/env python
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
	print '00:[' + i.name + ']'

	i.name = 'modified name'
	print '01:[' + i.name + ']'

	i.setname('new name')
	print '02:[' + i.getname() + ']'

main()

