# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext as _

from complaint.models import Complaint


class ComplaintForm(ModelForm):

    class Meta:
        model = Complaint
        fields = ['name', 'consumer_number', 'sender_email', 'mobile_number', 'landline_number', 'address', 'complaint_type', 'complaint_detail']
        labels = {
            'name': _('Name'),
            'consumer_number': _('Consumer Number'),
            'sender_email': _('Email'),
            'mobile_number': _('Mobile Number'),
            'landline_number': _('Landline Number'),
            'complaint_type': _('Type of Compalint'),
            'address': _('Delivery Address'),
            'complaint_detail': _('Complaint Matter')
        }
        widgets = {
            'complaint_detail': Textarea(attrs={'placeholder': _('Enter your complaint here.')})
        }
    
    def clean_data(self):
        for key in self.data.keys():
            self.data[key] = self.data[key].strip()
        return self.data
