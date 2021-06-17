from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def main(request):
    return HttpResponse("Welcome to the Django ! ")

def runoob(request):
    context = {}
    context['hello'] = 'Hello Template!'
    return render(request, 'runoob.html', context)

def runoob1(request):
    views_name = "菜鸟教程"
    return render(request, "runoob1.html", {"name": views_name})