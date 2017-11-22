from django.shortcuts import render
from django.http import HttpResponse
from myweb.models import Types,Goods,Recommend
from django.core.paginator import Paginator

# Create your views here.

def loadinfo():
	context = {}
	context['type0list'] = Types.objects.filter(pid=0)
	return context
#首页
def index(request):
	context = loadinfo()
	mobiles = Goods.objects.filter(typeid = 20)
	mobiles = mobiles.order_by('-store')[0:9]
	recommend = Recommend.objects.filter()[0:9] #推荐商品
	strip = Goods.objects.filter(typeid = 21)
	strip = strip.order_by('store')[0:9]
	context['mobiles'] = mobiles
	context['strip']=strip
	context['recommend']=recommend
	return render(request,'myweb/index.html',context)
#列表页
def list(request,pIndex):
	context = loadinfo()
	list1 = Goods.objects.filter()
	if request.GET.get('tid','') !='': #获取属性tid的值
		tid = str(request.GET.get('tid',''))
		list1 = list1.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
	p = Paginator(list1,8)
	#判断页号没有值时初始化为1
	if pIndex == '':
		pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	# context = {'orderlist':list2,'plist':plist,'pIndex':pIndex}
	context['goodslist'] = list2
	context['plist']=plist
	context['pIndex']=pIndex
	return render(request,'myweb/list.html',context)
#详情页
def detail(request,gid):
	context = loadinfo()
	goods = Goods.objects.get(id = gid)
	goods.clicknum += 1
	goods.save()
	context['goods'] = goods
	return render(request,'myweb/detail.html',context)