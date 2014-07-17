# :encoding: utf-8

import django
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore

# Create your views here.




def main(request):

	#
	# 単純な文字列を返却するアクションの例
	#

	session_id = get_session_id(request)
	user_name = get_session(request, 'user')
	# s = SessionStore(session_key = '')
	if False:
		return django.http.HttpResponse(
				'hello user_name=[' + str(user_name) + ']' +
				', session_id=[' + str(session_id) + ']')
	template = django.template.loader.get_template('index.html')
	fields = { 'x_user_name': user_name }
	context = django.template.RequestContext(request, fields)
	return django.http.HttpResponse(template.render(context))

def get_session_id(request):
	
	try:
	
		# session_id = request.session['session.id']
	
		# session = SessionStore()
		session_id = request.session.session_key
		if session_id == '' or session_id == None:
			# request.session = SessionStore() #不要
			request.session.save()
			session_id = request.session.session_key

		return session_id
	
	except:

		# session_id = uuid.uuid1()
		# session_id = str(session_id)
		# request.session['session.id'] = session_id
		# return session_id

		s = SessionStore()
		s.save()
		return s.session_key

def get_session(request, item_name):
	try:
		return request.session[item_name]
	except Exception, e:
		return None

def try_login(request):
	user_name = request.POST['login.user']
	if len(user_name) == 0:
		return False
	request.session['user'] = user_name
	return True

def login(request):

	#
	# ログインページ的なもの
	#
	if request.method == 'POST':
		if try_login(request):
			return django.http.HttpResponseRedirect('/')
	template = django.template.loader.get_template('login.html')
	fields = {}
	context = django.template.RequestContext(request, fields)
	return django.http.HttpResponse(template.render(context))














def hello(request):

	#
	# テンプレートを利用したアクションの例
	#

	template = django.template.loader.get_template('hello.html')
	fields = {}
	context = django.template.RequestContext(request, fields)
	return django.http.HttpResponse(template.render(context))










