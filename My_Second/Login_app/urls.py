from django.urls import re_path as url
from django.urls import path 
from Login_app import views 

app_name = 'Login_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login_page, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='logout'),
]