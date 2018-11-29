from django.shortcuts import render,HttpResponse
from .models import User
import json
# Create your views here.

def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = User.objects.filter(userName=username).filter(passWord=password)
    result = {}
    if user:
        result['msg']='登录成功'
        result['username'] = username
        result['password'] = password
        #把字典转换成json        
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        result['msg']='用户名或者密码错误'
        result['username'] = username
        result['password'] = password
        #把字典转换成json        
        result = json.dumps(result)
        return HttpResponse(result)
