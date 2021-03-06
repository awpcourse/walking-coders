"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from SocialApp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.HomeView.as_view(),  name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^editProfile/$', views.EditProfileView.as_view(), name='editProfile'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^message/$', views.MessageView.as_view(), name='message'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^companies/$', views.CompanyView.as_view(), name='companies'),
    url(r'^logout/$', views.logout_view, name='logout')
]
