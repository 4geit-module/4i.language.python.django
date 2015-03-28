# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from select_multiple_field.models import SelectMultipleField

class Category(models.Model):
    name = models.CharField(_('name'), max_length=200)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Product(models.Model):
    name = models.CharField(_('name'), max_length=200)
    quantity = models.IntegerField(_('quantity'))
    STATUS_CHOICES = (
        ('preparation', _('Preparation')),
        ('validated', _('Validated')),
        ('pending', _('Pending')),
        ('applied', _('Applied')),
        ('failed', _('Failed')),
    )
    status = models.CharField(_('status'), choices=STATUS_CHOICES, max_length=200, default='preparation')
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True, null=True)
    date_created = models.DateTimeField(_('date_created'), auto_now_add=True)
    date_last_modified = models.DateTimeField(_('date_last_modified'), auto_now=True)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

