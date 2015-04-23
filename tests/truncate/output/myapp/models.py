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
        
    :param body: 
    :type body: text
        
    :param date_created: 
    :type date_created: datetime
        
    :param date_last_modified: 
    :type date_last_modified: datetime
    """

    name = models.CharField(_('name'), max_length=200)
    quantity = models.IntegerField(_('quantity'))
    body = models.TextField(_('body'))
    date_created = models.DateTimeField(_('date_created'), auto_now_add=True)
    date_last_modified = models.DateTimeField(_('date_last_modified'), auto_now=True)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

