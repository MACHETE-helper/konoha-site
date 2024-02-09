from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('hokage', views.hokage, name='hokage'),
    path('teachers', views. teachers, name='teachers')

] + static(settings.STATIC_URL)