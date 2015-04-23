# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.contenttypes.models import ContentType

class ProductTag(models.Model):
    """
    ProductTag
        
    :param tag: 
    :type tag: slug
        
    :param product: 
    :type product: foreignkey
    """

    tag = models.SlugField(_('tag'), max_length=200)
    product = models.ForeignKey('Product', verbose_name=_('product'))

    def save(self, *args, **kwargs):
        super(ProductTag, self).save(*args, **kwargs)

    def __unicode__(self):
        return """Tag (%d)""" % self.id

class ProductKeyword(models.Model):
    """
    ProductKeyword
        
    :param keyword: 
    :type keyword: slug
        
    :param quantity: 
    :type quantity: int
        
    :param product: 
    :type product: foreignkey
    """

    keyword = models.SlugField(_('keyword'), max_length=200)
    quantity = models.IntegerField(_('quantity'), default=0)
    product = models.ForeignKey('Product', verbose_name=_('product'))

    def save(self, *args, **kwargs):
        super(ProductKeyword, self).save(*args, **kwargs)

    def __unicode__(self):
        return """Keyword (%d)""" % self.id

class Product(models.Model):
    """
    Product
        
    :param name: 
    :type name: char
    """

    name = models.CharField(_('name'), max_length=200)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

