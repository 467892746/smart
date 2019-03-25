from django.http import HttpResponse
from django.shortcuts import redirec


def inde(request):
    return HttpResponse('index')


def login(request):
    return redirect('/index')
