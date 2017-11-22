from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myweb.models import Goods,Detail,Orders,Users,Types
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import time,datetime,json
#首页
def loadinfo():
	context = {}
	context['type0list'] = Types.objects.filter(pid=0)
	return context

def cart(request):
	context = loadinfo()
	if 'shoplist' not in request.session:
		request.session['shoplist']={}
	dicts = request.session['shoplist']
	if dicts == {}:
		request.session['shoplist']={}
	context['info'] ='' #提交时判断购物车是否为空
	return render(request,'myweb/cart.html',context)

#向购物车中添加商品
def cartadd(request,gid):
	print(gid)
	goods = Goods.objects.get(id=gid)
	shop=goods.doGoods()
	print(shop)
	shop['num']=int(request.POST['num'])
	print(shop)
	#获取原购物车中的信息
	if 'shoplist' in request.session:
		shoplist = request.session['shoplist']
	else:
		shoplist={}
	#判断并放置到session中
	if gid in shoplist:
		shoplist[gid]['num'] +=int(request.POST['num']) #若购物车中已经有该id商品,则将该商品的数量加
	else:
		shoplist[gid] = shop #若不存在该id商品,就将该商品加入购物车中
	#将购物车中添加到session中
	request.session['shoplist'] = shoplist
	lists = len(request.session['shoplist'].keys())
	print(lists)
	return redirect(reverse('myweb_cart'))

#删除购物车的信息
def cartdel(request,gid):
	#获取购物车中信息
	shoplist = request.session['shoplist']
	#删除对应的商品
	del shoplist[gid]
	#将购物车的信息放回session中
	request.session['shoplist'] = shoplist
	return redirect(reverse('myweb_cart'))
#清空购物车
def cartclear(request):
	request.session['shoplist']={}
	return redirect(reverse('myweb_cart'))

#更改商品的数量
def cartchange(request):
	shoplist = request.session['shoplist']
	#获取商品的信息
	gid = request.GET['sid']
	num = int(request.GET['num'])
	if num<1:
		num =1
	shoplist[gid]['num']=num  #更改上商品的数量
	request.session['shoplist']=shoplist
	return redirect(reverse('myweb_cart'))


#订单处理
def order(request):
	context = loadinfo()
	#获取选定后的商品的id号
	strs = request.GET.get('gids','')
	if strs == '':
		list1 = ['购物车空空']
		context['info'] = json.dumps(list1)
		return render(request,'myweb/cart.html',context)
	#获取购物车中的信息
	else:
		lists = strs.split(',')
		shoplist = request.session['shoplist']
		orderlist = {}
		total = 0
		for oid in lists:
			orderlist[oid] = shoplist[oid]
			# print(orderlist)
			#计算商品的总价格
			total += shoplist[oid]['price']*shoplist[oid]['num']
		#将选中商品的信息放入订单中
		request.session['orderlist'] = orderlist
		request.session['total'] = total
		print(request.path)
		return render(request,'myweb/order.html',context)
#确认订单
def confirmorder(request):
	context = loadinfo()
	order = {
	'linkman':request.POST['linkman'],
	'address':request.POST['address'],
	'code':request.POST['code'],
	'phone':request.POST['phone'],
	}
	context['user'] = order
	return render(request,'myweb/confirmorder.html',context)
#添加订单信息
def add_orders(request):
	#将信息添加到订单表中
	try:
		ob = Orders()
		ob.uid = request.session['myweblogin']['id']
		ob.linkman = request.POST['linkman']
		ob.address = request.POST['address']
		ob.code = request.POST['code']
		ob.phone = request.POST['phone']
		ob.total = request.session['total']
		ob.addtime = time.time()
		ob.status = 0
		ob.save()
		shoplist = request.session['shoplist']
		lists = request.session['orderlist']
		#遍历购物信息并添加订单详情
		for gid in lists:
			dd = Detail()
			dd.orderid = ob.id
			dd.goodsid = gid
			dd.name = shoplist[gid]['goods']
			dd.price = shoplist[gid]['price']
			dd.num = shoplist[gid]['num']
			dd.picname = shoplist[gid]['picname']
			dd.save()
			#添加商品的购买次数
			goods = Goods.objects.get(id = gid)
			goods.num = shoplist[gid]['num']
			goods.store = goods.store - shoplist[gid]['num']
			goods.save()
			#删除购物车中选中的商品信息
			del shoplist[gid]
		request.session['shoplist'] = shoplist
		#删除总价格
		del request.session['total']
		# 下单时间
		# buytime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
		# print(lists)
		# context = {'shoplist':lists,'buytime':buytime,'oldtime':int(ob.addtime)}
		return redirect(reverse('myorder'))
	except:
		context = loadinfo()
		list1 = ['下单单失败']
		context['info'] =json.dumps(list1)
		return render(request,'myweb/cart.html',context)

#我的订单
def myorder(request):
	context = loadinfo()
	ob = Orders.objects.filter(uid = request.session['myweblogin']['id'])
	orderinfo = []
	for orders in ob:
		od = orders.doOrders()
		print(od)
		orderinfo.append(od)
	# print(orderinfo)
	context['orderinfo'] = orderinfo
	# context = {'orderinfo':orderinfo}
	return render(request,'myweb/member/myorder.html',context)
#待发货表单
def await(request,oid):
	context = loadinfo()
	details = Detail.objects.filter(orderid = oid)
	detailinfo = []
	for detail in details:
		detaildict = detail.doDetail()
		detailinfo.append(detaildict)
	print(detailinfo)
	context['detailinfo'] = detailinfo
	context['orderid'] = oid
	# context = {'detailinfo':detailinfo,'orderid':oid}
	return render(request,'myweb/await.html',context)

#个人中心
def member(request):
	context = loadinfo()
	orderlist = Orders.objects.filter(uid = request.session['myweblogin']['id'])
	orders = orderlist.filter(status=0)#未发货订单
	order = orderlist.filter(status=1) #统计已发货订单
	num = 0 #统计未发货的数量
	num2 = 0 #统计已发货订单
	num = orders.count()
	num2 = order.count()
	context['num']=num
	context['num2']=num2
	return render(request,'myweb/member/member.html',context)

#加载个人信息
def editmember(request):
	try:
		context = loadinfo()
		member = Users.objects.get(id = request.session['myweblogin']['id'])
		context['member'] = member
		context['info'] = ''
		# context = {'member':member,'info':''}
		return render(request,'myweb/member/editmember.html',context)
	except:
		list1 = ['加载失败']
		context['info'] = json.dumps(list1)
		# context = {'info':json.dumps(list1)}
		return render(request,'myweb/member/editmember.html',context)

#修改个人信息
def updatemember(request):
	try:
		member = Users.objects.get(id = request.session['myweblogin']['id'])
		member.sex = request.POST['sex']
		member.address = request.POST['address']
		member.code = request.POST['code']
		member.phone = request.POST['phone']
		member.email = request.POST['email']
		member.save()
		return redirect(reverse('member'))
	except:
		context = loadinfo()
		list1 = ['修改失败']
		context['info'] =json.dumps(list1)
		return render(request,'myweb/member/editmember.html',context)
#订单状态的修改
def staorder(request,state,oid):
	if state == '0':
		order = Orders.objects.get(id=oid)
		print('ok')
		order.delete()
		details = Detail.objects.filter(orderid = oid)
		for detail in details:
			detail.delete()
	elif state == '1':
		order = Orders.objects.get(id = oid)
		order.status = 2
		order.save()
	return redirect(reverse('myorder'))
