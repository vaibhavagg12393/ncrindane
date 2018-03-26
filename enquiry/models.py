# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Enquiry(models.Model):

    name = models.CharField(max_length=100, blank=False)
    sender_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=False)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=280)
    query = models.TextField(blank=False)

    def __unicode__(self):
        return _(u'Name: {name}, Phone: {phone_number}').format(
            name=self.name, phone_number=self.phone_number)