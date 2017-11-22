from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myadmin.models import Users,Goods,Orders,Detail,Recommend
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
import json
#获取订单信息
def orders(request,pIndex):
	ob = Orders.objects.filter()
	#判断并封装搜索条件
	where = [] #定义一个用于封装的搜索条件
	if request.GET.get('name','') !='':
	    ob = ob.filter(linkman__contains=request.GET.get('name'))
	    print(ob)
	    where.append('name='+request.GET.get('name'))
	p = Paginator(ob,5)
	#判断页号没有值时初始化为1
	if pIndex == '':
		pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	context = {'orderlist':list2,'plist':plist,'pIndex':pIndex,'where':where}
	return render(request,'myadmin/orders/index.html',context)
#加载详情页面
def detail(request,oid):
	detaillist = Detail.objects.filter(orderid = oid)
	context = {'detaillist':detaillist,'info':''}
	return render(request,'myadmin/orders/detail.html',context)

#加载编辑页面
def editorder(request,oid):
	order = Orders.objects.get(id = oid)
	context = {'order':order,'info':''}
	return render(request,'myadmin/orders/edit.html',context)
#执行编辑页面
def updateorder(request,oid):
	order = Orders.objects.get(id = oid)
	order.status = request.POST['status']
	order.save()
	# list1 = ['修改成功']
	# context = {'info':json.dumps(list1)}
	return redirect(reverse('myadmin_orders',args=[1]))

