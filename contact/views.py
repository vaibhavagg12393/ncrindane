# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class ContactView(TemplateView):

    template_name = "contact/contact_base.html"
