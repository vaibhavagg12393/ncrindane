# -*- coding: utf-8 -*-

from django.conf.urls import url

from app.views import AlbumDetail, gallery


urlpatterns = [
    url(r'^$', gallery, name='gallery'),
    url(r'^(?P<slug>[-\w]+)$', AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()
]
