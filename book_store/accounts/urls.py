from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]