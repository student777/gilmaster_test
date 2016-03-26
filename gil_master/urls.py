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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gil_master.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'gil_master.views.detail', name='detail'),
    url(r'^new/$', 'gil_master.views.new', name='new'),
    url(r'^test/$', 'gil_master.views.test', name='test'),
    url(r'^test2/$', 'gil_master.views.test2', name='test2'),
    url(r'^(?P<pk>\d+)/edit/$', 'gil_master.views.edit', name='edit'),
    url(r'^(?P<pk>\d+)/comment/new/$', 'gil_master.views.comment_new', name='comment_new'),
    url(r'^(?P<pk>\d+)/delete/$', 'gil_master.views.delete', name='delete'),
    url(r'^(?P<pk>\d+)/(?P<comment_pk>\d+)/comment/delete/$', 'gil_master.views.comment_delete', name='comment_delete'),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
            })
    ]
