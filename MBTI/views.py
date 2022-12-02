from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def MBTI(request):
    user_id = request.session.get('user')
    if request.method == "GET":
        return render(request, 'MBTI.html')
    else:
        user = User.objects.get(id=user_id)
        mbti = request.POST.get('mbti', '')
        user.mbti = mbti
        user.save()
        return redirect('/')


def user(request):
    if request.method == "GET":
        return render(request, 'user.html')
    else:
        user = request.POST.get('user')
        user = User(user=user)
        user.save()
        # User.objects.create(user=user)
        request.session['user'] = user.id
        return redirect('MBTI/')