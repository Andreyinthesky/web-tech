"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

app_urls = 'qa.urls'

urlpatterns = [
    url(r'^$', include(app_urls)),
    url(r'^login/.*$', include(app_urls), name='login'),
    url(r'^signup/.*', include(app_urls), name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', include(app_urls), name='question'),
    url(r'^ask/.*', include(app_urls), name='ask'),
    url(r'^popular/.*', include(app_urls), name='popular'),
    url(r'^new/.*', include(app_urls), name='new'),
]
