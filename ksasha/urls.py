from django.urls import path
from . import views

urlpatterns = [
    path('',views.myhome,name='myhome'),
    path('Register/',views.Register,name='Register'),
     path('login_user',views.login_user,name='login_user'),
]

