# gsd main
from django.shortcuts import render, redirect

def main(request):
    if 'user_id' not in request.session:
        return redirect('/landing')
    print("hello")
    return render(request, 'main.html')

def logout(request):
    request.session.clear()
    return redirect('/landing')
