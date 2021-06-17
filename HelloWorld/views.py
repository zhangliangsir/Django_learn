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

def runoob_list(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "runoob_list.html", {"views_list": views_list})

def runoob_default(request):
    name = 0

    import datetime
    now = datetime.datetime.now()
    return render(request, "runoob_default.html", {"name": name, "time": now})

def runoob_safe(request):
    views_str = "<a href='https://github.com/zhangliangsir/Django_learn'>github</a>"
    return render(request, "runoob_safe.html", {"views_str": views_str})