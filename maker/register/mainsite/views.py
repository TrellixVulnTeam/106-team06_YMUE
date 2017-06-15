from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from mainsite import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
# Create your views here.

def first(request):
    template = get_template('first.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)
def second(request):
    template = get_template('second.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)
def third(request):
    template = get_template('third.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)
def forth(request):
    template = get_template('forth.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)
def fifth(request):
    template = get_template('fifth.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)

def index(request):
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)

def information(request):
    template = get_template('Information.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)
    
def index1(request, pid=None, del_pass=None):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        try:
            user = models.User.objects.get(username=username)
            diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)
    
    template = get_template('index1.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)

@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
    user = User.objects.get(username=username)
    try:
        profile = models.Profile.objects.get(user=username)
    except:
        profile = models.Profile(user=user)

    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            messages.add_message(request, messages.INFO, "個人資料已儲存")
            profile_form.save()  
            return HttpResponseRedirect('/userinfo')
        else:
            messages.add_message(request, messages.INFO, '要修改個人資料，每一個欄位都要填...')
    else:
        profile_form = forms.ProfileForm()
#    return render(request, 'userinfo.html',context)
    template = get_template('userinfo.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
#    html = template.render(locals())
    return HttpResponse(html)


def login(request):
    if request.user.is_authenticated():
        return redirect('/')
    user = request.user.username
    if request.method == 'POST':    
        login_form = forms.LoginForm(request.POST)
    #    form = authentication_form(request, data=request.POST)
        if login_form.is_valid():
            login_name=request.POST['username']
            login_password=request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO,'請檢查輸入的欄位內容')
    else:
         login_form = forms.LoginForm() 
         user = ""
         return render_to_response('login.html')
        

    context = { "user": user }
    return render(request, "login.html", context)

    template = get_template('login.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
   # return HttpResponse(html)

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出了")
    return redirect('/')

@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        userpassword = request.user.password
    messages.get_messages(request)
        
    if request.method == 'POST':
        user = models.User.objects.get(name=username)
       # if user == NULL:
       #    user = models.User.objects._create_user(name=username, email=useremail, password='123456')
        diary = models.Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "日記已儲存")
            post_form.save()  
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, '要張貼日記，每一個欄位都要填...')
    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, '要張貼日記，每一個欄位都要填...')

    template = get_template('posting.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(locals())
    return HttpResponse(html)
