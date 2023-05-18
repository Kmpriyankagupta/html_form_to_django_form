from django.urls import path, include
from newapp import views

urlpatterns = [
    
    path('', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('index', views.index, name='index'),
    path('logout_view', views.logout_view, name='logout_view'),
    #path('login_user/logout1', views.logout1, name = 'logout')
    #path('logout_user', views.logout_user, name='logout_user')
]