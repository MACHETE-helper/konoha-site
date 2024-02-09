from django.shortcuts import render
from.models import Articles
from django.http import HttpResponse

def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})
