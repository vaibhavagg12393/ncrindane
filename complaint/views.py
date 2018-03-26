# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from forms import ComplaintForm
from models import Complaint


class ComplaintFormView(FormView):

    template_name = "complaint/complaint_form.html"
    form_class = ComplaintForm
    success_url = '/complaint/success/'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        return super(ComplaintFormView, self).form_valid(form)


class ComplaintFormSuccessView(TemplateView):

    template_name = "complaint/complaint_success.html"