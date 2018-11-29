from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Question,Choice,User
import json
# Create your views here.
#展示所有问题
# def index(request):
#     question_list = Question.objects.all()
#     return render(request,'index.html',{'ql':question_list})

def index(request):
    question_list = Question.objects.all()
    datas={}
    re={}
    if question_list:
        for q in question_list:
            datas[q.id]=q.question_text
        re['status']='200'
        re['msg']='success'
        re['data']= datas
        r=json.dumps(re)#转换为json格式
        return HttpResponse(r)
    else:
        re['status']='10021'
        re['msg']='null'
        re['data']= datas
        r=json.dumps(re)#转换为json格式
        return HttpResponse(r)


#显示某个问题下的选项
# def detail(request,question_id):
#     #如果没有object返回404，pk是主键(根据主键某一个question)
#     q = get_object_or_404(Question,pk=question_id)
#     return render(request,'detail.html',{'q':q})

def detail(request,question_id):
    choices = Choice.objects.filter(question_id=question_id)
    datas={}
    re={}
    if choices:
        for q in choices:
            datas[q.id]=q.choice_text
        re['status']='200'
        re['msg']='success'
        re['data']= datas
        r=json.dumps(re)#转换为json格式
        return HttpResponse(r)
    else:
        re['status']='10021'
        re['msg']='null'
        re['data']= datas
        r=json.dumps(re)#转换为json格式
        return HttpResponse(r)



#投票
# def vote(request,question_id):
#     q = get_object_or_404(Question,pk=question_id)
#     choiceid = request.POST.get("choice")
#     SelectChoice = q.choice_set.get(pk=choiceid)
#     SelectChoice.votes += 1
#     SelectChoice.save()
#     return render(request,'result.html',{'q':q})

##投票-自己写的
# def vote(request,question_id):
#     choices = Choice.objects.filter(question_id=question_id)
#     choiceid = request.POST.get("choice")
#     votes = Choice.objects.filter(votes=choiceid)
#     datas={}
#     re={}
#     if choices:
#         for q in choices:
#             datas[q.choice_text]=q.votes
#         re['status']='200'
#         re['msg']='success'
#         re['data']= datas
#         r=json.dumps(re)#转换为json格式
#         return HttpResponse(r)
#     else:
#         re['status']='10021'
#         re['msg']='null'
#         re['data']= datas
#         r=json.dumps(re)#转换为json格式
#         return HttpResponse(r)


##投票-老师讲的
def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    choiceid = request.POST.get("choice",'')
    response_data={}
    if choiceid=='':
      response_data["status"]='10021'
      response_data["msg"]='null'
      result=json.dumps(response_data)
      return HttpResponse(result)
    try:
        selected_choice=p.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        response_data["status"]='10022'
        response_data["msg"]='没有这个选项'
        result=json.dumps(response_data)
        return HttpResponse(result)
    else:
        selected_choice.votes+=1
        selected_choice.save()
        response_data['status']='200'
        response_data['msg']='success'
        result=json.dumps(response_data)
        return HttpResponse(result)
#登录接口
def login(request):
    username=request.POST.get("username",'')
    password=request.POST.get("password",'')
    users=User.objects.filter(userName=username,passWord=password)
    response_data={}
    if list(users)==[]:
        response_data["status"]='10021'
        response_data["msg"]='用户名或密码错误'
        result=json.dumps(response_data)
        return HttpResponse(result)
    else:
        response_data["status"]='200'
        response_data["msg"]='登录成功'
        result=json.dumps(response_data)
        return HttpResponse(result)