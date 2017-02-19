"""hackathon URL Configuration

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
from django.conf import settings
from gil_master import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^test/$', views.test, name='test'),
    url(r'^test2/$', views.test2, name='test2'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<pk>\d+)/(?P<comment_pk>\d+)/comment/delete/$', views.comment_delete, name='comment_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)