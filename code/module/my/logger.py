import datetime

def info(*args):
	print(datetime.datetime.now(), " [INFO] ", *args, sep="")
