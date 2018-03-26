# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from forms import EnquiryForm
from models import Enquiry


class EnquiryFormView(FormView):

    template_name = "enquiry/enquiry_form.html"
    form_class = EnquiryForm
    success_url = '/enquiry/success/'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        return super(EnquiryFormView, self).form_valid(form)


class EnquiryFormSuccessView(TemplateView):

    template_name = "enquiry/enquiry_success.html"