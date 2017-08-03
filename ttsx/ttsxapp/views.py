#encoding=utf-8
from django.shortcuts import render,redirect
from models import UserInfo
from hashlib import sha1
from django.http import JsonResponse
import datetime
from user_decorators import user_login

def index(request):
    context={'title':'首页'}
    return render(request,'user/index.html',context)

def login(request):
    context={'title':'注册','top':'0'}
    return render(request,'user/login.html',context)

def register(request):
    context={'title':'注册','top':'0'}
    return render(request,'user/register.html',context)

def register_handle(request):
    dict=request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    upwd1 = dict.get('cpwd')
    uemail = dict.get('email')
    print '---------------------------'
    if upwd != upwd1:
        return redirect('/user/register/')
    user = UserInfo()
    user.uname = uname

    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()

    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')

def check_name(request):

    name = request.POST.get('uname')
    # print name
    chk_name = UserInfo.objects.filter(uname=name)
    # print chk_name
    if chk_name:
        # print chk_name
        return JsonResponse({'dict': '1'})
    else:
        # print chk_name
        return JsonResponse({'dict': '0'})

def login_handle(request):
    login_data = request.POST
    uname = login_data.get('username')
    upwd = sha1(login_data.get('pwd')).hexdigest()
    ucheckbox = login_data.get('checkbox','0');
    # uemail = login_data.get('uemail')
    print ucheckbox
    # print uname
    # print upwd
    chk_login = UserInfo.objects.filter(uname=uname)
    print '-----------'
    # print chk_login[0].uname
    # print chk_login[0].upwd

    if len(chk_login) == 0:
        context = {'display': 'block'}
        return render(request,'user/login.html',context)
    elif chk_login[0].upwd != upwd:
        context={'display':'block'}
        return render(request, 'user/login.html',context)
    elif chk_login[0].upwd == upwd:
        request.session['id'] = chk_login[0].id
        request.session['name'] = uname
        path = request.session.get('url_path', '/user/center/')
        print path
        response = redirect(path)
        print '22222222'
        if ucheckbox == '1':
            response.set_cookie('uname',uname,expires=datetime.datetime.now()+datetime.timedelta(days=7))
            print '333333333333333'
        else:
            response.set_cookie('uname','',max_age=-1)
        return response
        # return render(request,'user/center.html')

def logout(request):
    request.session.flush()
    return redirect('/user/login/')


# @user_login
def center(request):
    if  request.session.has_key('id'):
        user = UserInfo.objects.get(pk=request.session['id'])
        context = {'title': '用户中心','user':user}
        print '111111111122222222222'

        # print user[0].uemail
        print request.session.get('name')
        return render(request,'user/center.html',context)
    else:
        return redirect('/user/login/')
@user_login
def site(request):
    user = UserInfo.objects.get(pk=request.session['id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '收货地址', 'user': user}
    return render(request, 'user/site.html', context)

# @user_login
def order(request):
    context={'title':'用户订单'}
    return render(request,'user/order.html',context)





