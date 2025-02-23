from django.contrib import admin
from django.urls import path
from .views import say_hello, index

urlpatterns = [
    #path('', say_hello, name='sayHello'),
    path('', index, name='index'),
]