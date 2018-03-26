# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views as faq_views

urlpatterns = [
    url(
        regex = r'^$',
        view  = faq_views.TopicList.as_view(),
        name  = 'faq_topic_list',
    ),
    url(
        regex = r'^(?P<slug>[\w-]+)/$',
        view  = faq_views.TopicDetail.as_view(),
        name  = 'faq_topic_detail',
    ),
]