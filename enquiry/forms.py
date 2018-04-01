# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext as _

from models import Enquiry


class EnquiryForm(ModelForm):

    class Meta:
        model = Enquiry
        fields = ['name', 'sender_email', 'phone_number', 'company', 'address', 'query']
        labels = {
            'name': _('Name'),
            'sender_email': _('Email'),
            'phone_number': _('Phone Number'),
            'company': _('Company'),
            'address': _('Address'),
            'query': _('Query')
        }
        widgets = {
            'query': Textarea(attrs={'placeholder': _('Enter your query here.')})
        }
    
    def clean_data(self):
        for key in self.data.keys():
            self.data[key] = self.data[key].strip()
        return self.data
