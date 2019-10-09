#!/usr/bin/python3

import psycopg2
import datetime

def dump(datetime):
	print("[TRACE] the datetime is ", "{0:%Y-%m-%d %H:%M:%S.%f}".format(datetime), sep="")
	print("[TRACE] the datetime is ", "{0:%F}".format(datetime), sep="")

def get_connection():

	connection = psycopg2.connect(
		host="127.0.0.1", user="user1", password="password", database="testdb", port=5432)
	connection.set_client_encoding("utf-8")
	return connection

def main():

	connection = get_connection()

	cur = connection.cursor()
	cur.execute("SELECT current_timestamp WHERE 1 = %s", "1")
	for row in cur:
		dump(row[0])
	cur.close()

	connection.close()

main()
