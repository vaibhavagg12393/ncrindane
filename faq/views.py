# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.db.models import Max
from django.views.generic import ListView, DetailView

from faq.models import Topic


class TopicList(ListView):
    model = Topic
    template = "faq/topic_list.html"
    allow_empty = True
    context_object_name = "topics"

    def get_context_data(self, **kwargs):
        data = super(TopicList, self).get_context_data(**kwargs)
        return data


class TopicDetail(DetailView):
    model = Topic
    template = "faq/topic_detail.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        # Include a list of questions this user has access to. If the user is
        # logged in, this includes protected questions. Otherwise, not.
        query_set = self.object.questions.filter(topic__slug=self.kwargs.get('slug'))
        if self.request.user.is_anonymous():
            query_set = query_set.exclude(protected=True)

        data = super(TopicDetail, self).get_context_data(**kwargs)
        data.update({
            'questions': query_set,
            'last_updated': query_set.aggregate(updated=Max('updated_on'))['updated'],
        })
        return data
