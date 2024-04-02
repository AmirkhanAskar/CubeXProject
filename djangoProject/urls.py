"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from cubexmain import views
from cubexmain.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Добавляем URL для HomeView
    path('about', views.about, name='about'),
    path('pricing', views.pricing, name='pricing'),
    path('features', views.features, name='features'),
    path('blog', views.blog, name='blog'),
    path('eachblog', views.eachblog, name='eachblog'),
    path('blogarticle', views.blogarticle, name='blogartcile'),
    path('integration', views.integration, name='integration'),
    path('login', views.account_login, name='login'),
    path('register', views.account_register, name='register'),

    path('login_user/', views.user_login, name='user-login'),
    path('logout_user/', views.user_logout, name='logout'),

    path('register_user/', views.register, name='register'),

    path('profile/', views.profile, name='profile'),

]
