def mydecorator(func):
	def inner_func(*args):
		print("[TRACE] <annotation> call: ", func, ", arguments: ", args, "", sep="")
		func(*args)
	return inner_func
