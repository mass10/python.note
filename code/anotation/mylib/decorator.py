def mydecorator(func):
	def inner_func(*args):
		func(*args)
	return inner_func
