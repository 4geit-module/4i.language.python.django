# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.contenttypes.models import ContentType

class Product(models.Model):
    """
    Product
        
    :param name: 
    :type name: char
        
    :param quantity: 
    :type quantity: int
        
    :param status: 
    :type status: choice
        
    :param date_created: 
    :type date_created: datetime
        
    :param date_last_modified: 
    :type date_last_modified: datetime
        
    :param progress: 
    :type progress: int
    """

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
    date_created = models.DateTimeField(_('date_created'), auto_now_add=True)
    date_last_modified = models.DateTimeField(_('date_last_modified'), auto_now=True)
    progress = models.IntegerField(_('progress'), blank=True, null=True)

    def __progressbar(self):
        progress = 0.
        size = 5
        if self.name: progress += 100./size
        if self.quantity: progress += 100./size
        if self.status: progress += 100./size
        if self.date_created: progress += 100./size
        if self.date_last_modified: progress += 100./size
        if self.progress: progress += 100./size
        return int(round(progress))

    def save(self, *args, **kwargs):
        self.progress = self.__progressbar()
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

