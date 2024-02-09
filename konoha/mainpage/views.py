from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'mainpage/welcome.html', {})
    #return HttpResponse("<h4>Проверка работы</h4>")

def about(request):
    return render(request, 'mainpage/about.html', {})

def price(request):
    return HttpResponse("<h4>Проверка работы. Цены</h4>")

def hokage(request):
    return HttpResponse("<h4>Проверка работы. Обо мне</h4>")

def teachers(request):
    return HttpResponse("<h4>Проверка работы. Учителя</h4>")