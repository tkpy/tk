from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myadmin.models import Users,Goods,Types,Recommend
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from PIL import Image
from django.core.paginator import Paginator
import time,os,json


#商品类别
def typeindex(request,pIndex=1):
    #执行数据查询,并放置到模板中
    types=Types.objects.extra(select = {"_has":"concat(path,id)"}).order_by('_has')
    #遍历查询结果,为每个结果对象追加一个pname属性,目的用于缩进标题
    p = Paginator(types,5)
    #判断页号没有值时初始化为1
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    for ob in list2:
        ob.pname = '...'*(ob.path.count(',')-1)
    context = {'typelist':list2,'plist':plist,'pIndex':pIndex}
    return render(request,'myadmin/types/index.html',context)
#商品类别信息添加表单
def typeadd(request,tid):
    #获取父类别信息,若没有则默认为跟类别信息
    if tid == "0":
        context = {'pid':0,'path':'0,','name':'跟类别'}
    else:
        ob = Types.objects.get(id = tid)
        context ={'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
    return render(request,'myadmin/types/add.html',context)
#执行商品类别信息添加
def typeinsert(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {'info':'添加成功'}
    except:
        context = {'info':'添加失败'}
    return render(request,'myadmin/info.html',context)

#执行商品类别信息删除
def typedel(request,tid):
    try:
        #获取被删除商品的子类别信息,若有数据,就禁止删除当前类别
        types = Types.objects.filter(pid = tid).count()
        if types > 0:
            context ={'info':'删除失败:次类别下还有子类别'}
            return render(request,'myadmin/info.html',context)
        ob =Types.objects.get(id=tid)
        ob.delete()
        return redirect(reverse('myadmin_typeindex',args=[1]))
    except:
        context = {'info':'删除失败'}
        return render(request,'myadmin/info.html',context)
#加载商品类别信息编辑表单
def typeedit(request,tid):
    try:
        types = Types.objects.get(id = tid)
        context = {"types":types}
        return render(request,'myadmin/types/edit.html',context)
    except:
        context = {"info":'没有获取到响应信息'}
        return render(request,'myadmin/info.html',context)
def typeupdate(request,tid):
    try:
        ob = Types.objects.get(id = tid)
        ob.name = request.POST['name']
        ob.save()
        context = {'info':'修改成功'}
    except:
        context = {'info':'修改失败'}
    return render(request,'myadmin/info.html',context)

    
#================商品信息管理=================
#加载商品信息表单
def goodsindex(request,pIndex=1):
    # nums = str(request.GET.get('typeid'))
    goods = Goods.objects.filter()
    lists = Types.objects.filter(pid=0)
    where = [] #定义一个用于维持搜索条件的变量
    if request.GET.get('goods','') != '':
        goods = goods.filter(goods__contains=request.GET.get('goods'))
        where.append('goods='+request.GET.get('goods'))
    if request.GET.get('typeid','') != '':
        tid=request.GET['typeid']
        goods = goods.filter(typeid__in=Types.objects.only('id').filter(path__contains = ','+tid+','))
        where.append('typeid='+request.GET.get('typeid'))
    #获取商品信息
    for ob in goods:
        ty = Types.objects.get(id = ob.typeid)
        ob.typename = ty.name
    p = Paginator(goods,5)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    #判断添加成功后session中是否由info信息
    if 'info' in request.session:
        list1 = [request.session['info']] #将session的值赋值给list1
        del request.session['info'] #删除session['info']内容
        context = {'typelist':lists,'goodslist':list2,'plist':plist,'pIndex':pIndex,'info':json.dumps(list1),'where':where}
        return render(request,'myadmin/goods/index.html',context)
    else:
        context = {'typelist':lists,'goodslist':list2,'plist':plist,'pIndex':pIndex,'info':'','where':where}
        return render(request,'myadmin/goods/index.html',context)
#加载添加商品信息表单
def goodsadd(request):
    #获取商品的类别信息
    listall = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    context = {'typelist':listall}
    return render(request,'myadmin/goods/add.html',context)
#执行添加商品信息表单
def goodsinsert(request):
    try:
        #执行图片的上传
        myfile = request.FILES.get("mypic",None)
        if not myfile:
            context = {'info':'请上传图片'}
            return render(request,'myadmin/info.html',context)
        filename = str(time.time())+"."+myfile.name.split('.').pop()
        fp = open("./static/myadmin/img/upload/"+filename,"wb+")
        for chunk in myfile.chunks():#分块写入文件
            fp.write(chunk)
        fp.close()
        #执行图片缩放
        im = Image.open("./static/myadmin/img/upload/"+filename)
        #缩放到75*75
        im.thumbnail((75,75))
        #把缩放后的图像用jpeg格式保存:
        im.save("./static/myadmin/img/upload/s_"+filename,None)
        
        #执行信息的添加
        ob = Goods()
        ob.typeid = request.POST['typeid']
        ob.goods = request.POST['goods']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.picname = filename
        ob.state = request.POST['state']
        ob.store = request.POST['store']
        ob.addtime = request.POST['addtime']
        ob.descr = request.POST['descr']
        ob.save()
        #将添加成功的信息放入session中
        request.session['info'] = '添加成功'
        return redirect(reverse('myadmin_goodsindex',args=[1]))
    except:
        request.session['info'] = '添加失败'
        return render(request,'myadmin/info.html',context)
#执行删除商品信息
def goodsdel(request,gid):
    try:
        goods = Goods.objects.get(id = gid)
        if goods.state == 2:
            context = {'info':'此商品正在销售,禁止删除'}
            return render(request,'myadmin/info.html',context)
        elif goods.state == 3:
            context = {'info':'此商品已下架,禁止删除'}
            return render(request,'myadmin/info.html',context)
        else:
            #执行图片的删除
            os.remove("./static/myadmin/img/upload/"+goods.picname)
            os.remove("./static/myadmin/img/upload/s_"+goods.picname)
            #执行数据删除
            goods.delete()
            return redirect(reverse('myadmin_goodsindex',args=[1]))
    except:
        context = {'info':'删除失败'}
        return render(request,'myadmin/info.html',context)
#加载修改商品信息表单
def goodsedit(request,gid):
    try:
        #获取要编辑的商品信息
        goods = Goods.objects.get(id = gid)
        #获取商品的类别信息
        listall = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
        context = {'good':goods,'typelist':listall}
        return render(request,'myadmin/goods/edit.html',context)
    except:
        context = {'info':'没有找到该信息'}
        return render(request,'myadmin/info.html',context)
#执行修改商品信息表单
def goodsupdate(request,gid):
    try:
        #执行图片的上传
        myfile = request.FILES.get("mypic",None)
        if not myfile:
            filename = request.POST['oldpicname']
        else:
            filename = str(time.time())+"."+myfile.name.split('.').pop()
            fp = open("./static/myadmin/img/upload/"+filename,"wb+")
            for chunk in myfile.chunks():#分块写入文件
                fp.write(chunk)
            fp.close()
            #执行图片缩放
            im = Image.open("./static/myadmin/img/upload/"+filename)
            #缩放到75*75
            im.thumbnail((75,75))
            #把缩放后的图像用jpeg格式保存:
            im.save("./static/myadmin/img/upload/s_"+filename,None)

        ob = Goods.objects.get(id = gid)
        ob.typeid = request.POST['typeid']
        ob.goods = request.POST['goods']
        ob.company = request.POST['company']
        ob.descr = request.POST['descr']
        ob.picname = filename
        ob.price = float(request.POST['price'])
        ob.state = request.POST['state']
        ob.store = request.POST['store']
        ob.addtime = request.POST['addtime']
        ob.save()
        context = {'info':'修改成功'}
        #判断删除老图片
        if myfile:
            os.remove("./static/myadmin/img/upload/"+request.POST['oldpicname'])
            os.remove("./static/myadmin/img/upload/s_"+request.POST['oldpicname'])
    except:
        context = {'info':'修改失败'}
        if myfile:
            os.remove("./static/myadmin/img/upload/"+picname)
            os.remove("./static/myadmin/img/upload/s_"+picname)
    return render(request,'myadmin/info.html',context)

def recommend(request,gid):
    goods = Goods.objects.get(id=gid)
    re = Recommend()
    re.id = goods.id
    re.typeisd = goods.id
    re.goods = goods.goods
    re.price = goods.price
    re.picname = goods.picname
    re.state = goods.state
    re.save()
    context = {'info':'推荐成功'}
    return render(request,'myadmin/info.html',context)

