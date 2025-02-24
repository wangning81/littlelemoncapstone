from operator import index
from django.urls import path
from .views import MenuItemView, SingleMenuItemView, index, say_hello
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('', say_hello, name='sayHello'),
    path('', index, name='index'),
    path('menu', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth', obtain_auth_token),
]