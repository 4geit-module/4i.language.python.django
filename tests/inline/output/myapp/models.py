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

class ProductTag(models.Model):
    tag = models.SlugField(_('tag'), max_length=200)

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return """Tag (%d)""" % self.id

class ProductKeyword(models.Model):
    keyword = models.SlugField(_('keyword'), max_length=200)
    quantity = models.IntegerField(_('quantity'), default=0)

    def save(self, *args, **kwargs):
        super(Keyword, self).save(*args, **kwargs)

    def __unicode__(self):
        return """Keyword (%d)""" % self.id

class Product(models.Model):
    name = models.CharField(_('name'), max_length=200)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

