from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import re

class AdminMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		# print('先看看有没有错')
		urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout','/myadmin/verify']
		#获取当前请求路径
		path = request.path
		#判断当前请求是否是访问网站后台,并且path不再URLlist中
		if re.match('/myadmin',path) and (path not in urllist):
			# print('试试先')
			#判断用户是否没有登录
			if "adminuser" not in request.session:
				#执行登录页面跳转
				return redirect(reverse('myadmin_login'))

		#网站前台登录验证判断
		if re.match("/order",path):
			#判断当前用户是否没有登录
			if 'myweblogin' not in  request.session:
				#执行登录界面(重定向)跳转
				return redirect(reverse('myweb_login'))

		response = self.get_response(request)
		return response