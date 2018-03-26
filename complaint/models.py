# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Complaint(models.Model):

    LEAKAGE = 'LEAK'
    LATE_DELIVERY = 'LATE'
    DELIVERY_MAN_COMPLAINT = 'MAN'
    OFFICE_STAFF_COMPLAINT = 'STAFF'
    OTHERS = 'OTHERS'

    COMPLAINT_TYPE = (
        (None, 'Select the type of Complaint'),
        (LEAKAGE, _('Leakage Problem')),
        (LATE_DELIVERY, _('Late Delivery')),
        (DELIVERY_MAN_COMPLAINT, _('Complaint against Delivery Man')),
        (OFFICE_STAFF_COMPLAINT, _('Complaint against Office Staff')),
        (OTHERS, _('Other'))
    )

    name = models.CharField(max_length=100, blank=False)
    consumer_number = models.CharField(max_length=20)
    sender_email = models.EmailField()
    mobile_number = models.CharField(max_length=10, blank=False)
    landline_number = models.CharField(max_length=10, blank=False)
    complaint_type = models.CharField(
        max_length=6,
        choices=COMPLAINT_TYPE,
        default=None,
        blank=False,
    )
    address = models.CharField(max_length=280)
    complaint_detail = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return _(u'Name: {name}, Consumer Number: {consumer_number}').format(
            name=self.name, consumer_number=self.consumer_number)