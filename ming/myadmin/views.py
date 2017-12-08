from django.shortcuts import render
from myadmin.models import Name,Stuname
from django.views.decorators.csrf import csrf_exempt # ajax请求解决问题
import json
from django.http import HttpResponse,JsonResponse
import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

# 请求数据
@csrf_exempt  # ajax请求语法糖
def doajax(request):
    namelist = Name.objects.all()
    lists = []
    for names in namelist:
        lists.append({'id':names.id,'name':names.name})
    return JsonResponse({'data':lists})

@csrf_exempt  #将请假的学生放入请假名单中
def vacate(request):
    # print(request.GET['nid'])
    stuname = Stuname()
    lists = Name.objects.get(id=request.GET['nid'])
    stuname.name = lists.name
    stuname.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(stuname.date)
    stuname.save()
    return JsonResponse({'data':1})

def show(request):
    showlist = Stuname.objects.all()
    content = {'showlist':showlist}
    return render(request,'vacate.html',content)
