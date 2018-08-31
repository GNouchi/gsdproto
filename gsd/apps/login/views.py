# gsd login 
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

REGISTRATION = 50
def landing(request):
    if 'user_id' in request.session:
        return redirect('/main')
    show_modal =""
    if 'show_modal' in request.session:
        show_modal = request.session['show_modal']
    context = {
        'show_modal' : show_modal
    }
    request.session.flush()
    print(context)
    return render(request, 'login.html', context)

def login(request):
    result = User.objects.loginValidator(request.POST)
    if len(result['errors']) > 0:
        for error in result['errors']:
            messages.error(request, error,extra_tags="login")
        request.session['show_modal']= "loginmodal"
        return redirect('/landing')
    request.session.flush()
    request.session['user_id'] = result['user_id']
    return redirect('/main')    

def registration(request):
    result = User.objects.regValidator(request.POST)
    if len(result['errors']) > 0:
        for error in result['errors']:
            messages.error(request, error, extra_tags="registration")
        request.session['show_modal']= "registermodal"
        return redirect('/landing')
    request.session.flush()
    request.session['user_id'] = result['user_id']
    return redirect('/main')