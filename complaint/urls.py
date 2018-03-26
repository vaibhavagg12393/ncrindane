# -*- coding: utf-8 -*-

from django.conf.urls import url

from complaint.views import ComplaintFormView, ComplaintFormSuccessView


urlpatterns = [
    url(r'^$', ComplaintFormView.as_view(), name='complaint-form'),
    url(r'^success/$', ComplaintFormSuccessView.as_view(), name='complaint-success'),
]
