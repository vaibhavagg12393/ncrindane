# -*- coding: utf-8 -*-

from django.conf.urls import url

from enquiry.views import EnquiryFormView, EnquiryFormSuccessView


urlpatterns = [
    url(r'^$', EnquiryFormView.as_view(), name='enquiry-form'),
    url(r'^success/$', EnquiryFormSuccessView.as_view(), name='enquiry-success'),
]
