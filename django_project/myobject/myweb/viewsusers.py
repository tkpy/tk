from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myweb.models import Users,Types
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
#首页
def loadinfo():
	context = {}
	context['type0list'] = Types.objects.filter(pid=0)
	return context
#加载登录界面
def login(request):
	list1 = []
	context = {'info':json.dumps(list1)}
	return render(request,'myweb/login.html',context)
#使用ajax验证手机号是否存在
@csrf_exempt
def alogin(request):
	if request.POST.get('username','') != '':
		ob = Users.objects.filter(username=request.POST['username']).count()
		context ={'data':ob}
		return JsonResponse(context)
	else:
		context = {'data':'用户名不能为空'}
		return JsonResponse(context)
#执行登录操作
def dologin(request):
	try:
		#先判断该用户是否存在
		ob = Users.objects.filter(username=request.POST['username']).count()
		if ob == 0:
			list1=['该用户不存在,请注册账号!']
			context = {'info':json.dumps(list1)}
			return render(request,'myweb/login.html',context)
		else:
			#获取用户信息
			users = Users.objects.get(username=request.POST['username'])
			#密码验证
			if users.state == 0 or users.state == 1:
				import hashlib
				m = hashlib.md5()
				m.update(bytes(request.POST['password'],encoding="utf8"))
				if users.password == m.hexdigest():
					#将当前用户信息添加到session中
					request.session['myweblogin']=users.douser()
					print(request.session['myweblogin'])
					return redirect(reverse('index'))
				else:
					list1 = ['登录密码错误']
					context = {'info':json.dumps(list1)}
					return render(request,'myweb/login.html',context)
			else:
				list1 = ['当前用户非管理员和会员用户']
				context = {'info':json.dumps(list1)}
				return render(request,'myweb/login.html',context)
	except:
		list1 = ['登录失败']
		context={'info':json.dumps(list1)}
		return render(request,'myweb/login.html',context)
#加载注册界面
def register(request):
	list1 = []
	context = {'info':json.dumps(list1)}
	return render(request,'myweb/register.html',context)
#执行会员添加操作
def addregister(request):
	try:
		users = Users()
		ob=Users.objects.filter(username=request.POST['username']).count()
		if ob != 0:
			list1 = ['该用户已存在,请重新注册']
			context={'info':json.dumps(list1)}
			return render(request,'myweb/register.html',context)
		else:
			users.addtime=1
			users.name=request.POST['name']
			users.address = 1
			users.username=request.POST['username']
			users.email=1
			users.phone = 1
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['password'],encoding="utf8"))
			users.password = m.hexdigest()
			users.save()
			# context = {"info":'注册成功'}
			return redirect(reverse('myweb_login'))
	except:
		list1 = ['注册失败']
		context = {"info":json.dumps(list1)}
		return render(request,'myweb/register.html',context)
#退出登录
def logout(request):
	del request.session['myweblogin']
	return redirect(reverse('index'))


