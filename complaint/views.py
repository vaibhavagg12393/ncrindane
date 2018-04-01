# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from forms import ComplaintForm
from models import Complaint

_COMPLAINT_TO_EMAIL = "COMPLAINT_TO_EMAIL"
class ComplaintFormView(FormView):

    template_name = "complaint/complaint_form.html"
    form_class = ComplaintForm
    success_url = '/complaint/success/'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        
        # name = form.cleaned_data['name']
        # consumer_number = form.cleaned_data['consumer_number']
        # sender_email = form.cleaned_data['sender_email']
        # mobile_number = form.cleaned_data['mobile_number']
        # landline_number = form.cleaned_data['landline_number']
        # complaint_type = form.cleaned_data['complaint_type']
        # address = form.cleaned_data['address']
        # complaint_detail = form.cleaned_data['complaint_detail']
        # if consumer_number or sender_email or mobile_number or landline_number or address:
        #     recipients = list(getattr(settings, _COMPLAINT_TO_EMAIL))
        #     subject = _compose_subject(complaint_type, consumer_number)
        #     message = _compose_message(form)
        #     msg = EmailMessage(subject, message, to=recipients)
        #     msg.content_subtype = "html"
        #     msg.send()

        return super(ComplaintFormView, self).form_valid(form)


class ComplaintFormSuccessView(TemplateView):

    template_name = "complaint/complaint_success.html"

# def _compose_subject(complaint_type, consumer_number):
#     return "COMPLAINT - "+ str(consumer_number) + " - " + str(complaint_type)

# def _compose_message(form):
#     name = form.cleaned_data['name']
#     consumer_number = form.cleaned_data['consumer_number']
#     sender_email = form.cleaned_data['sender_email']
#     mobile_number = form.cleaned_data['mobile_number']
#     landline_number = form.cleaned_data['landline_number']
#     complaint_type = form.cleaned_data['complaint_type']
#     address = form.cleaned_data['address']
#     complaint_detail = form.cleaned_data['complaint_detail']

#     message = ""
#     message += "<p><strong>Name:</strong> "+str(name)+"</p>" if name else ""
#     message += "<p><strong>Consumer Number:</strong> "+str(consumer_number)+"</p>" if consumer_number else ""
#     message += "<p><strong>Sender Email:</strong> "+str(sender_email)+"</p>" if sender_email else ""
#     message += "<p><strong>Mobile Number:</strong> "+str(mobile_number)+"</p>" if mobile_number else ""
#     message += "<p><strong>Landline Number:</strong> "+str(landline_number)+"</p>" if landline_number else ""
#     message += "<p><strong>Address:</strong> "+str(address)+"</p>" if address else ""
#     message += "<p><strong>Complaint Type:</strong> "+str(complaint_type)+"</p>" if complaint_type else ""
#     message += "<p><strong>Complaint:</strong> "+str(complaint_detail)+"</p>" if complaint_detail else ""

#     return message
