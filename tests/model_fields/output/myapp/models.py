# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.contenttypes.models import ContentType

class Category(models.Model):
    """
    Category
        
    :param name: 
    :type name: char
    """

    class Meta:
        verbose_name_plural = _('categories')

    name = models.CharField(_('name'), max_length=200, unique=True)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Tag(models.Model):
    """
    Tag
        
    :param name: 
    :type name: char
    """

    name = models.CharField(_('name'), max_length=200, unique=True)

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Author(models.Model):
    """
    Author
        
    :param name: 
    :type name: char
        
    :param email: 
    :type email: email
    """

    name = models.CharField(_('name'), max_length=200, unique=True)
    email = models.EmailField(_('email'), blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Product(models.Model):
    """
    Product
        
    :param name: 
    :type name: char
        
    :param slug: 
    :type slug: slug
        
    :param enabled: 
    :type enabled: bool
        
    :param category: 
    :type category: foreignkey
        
    :param author: 
    :type author: foreignkey
        
    :param tags: 
    :type tags: manytomany
        
    :param quantity: 
    :type quantity: int
        
    :param price: 
    :type price: float
        
    :param status: 
    :type status: choice
        
    :param description: 
    :type description: text
        
    :param picture: 
    :type picture: image
        
    :param date_created: 
    :type date_created: date
        
    :param date_last_modified: 
    :type date_last_modified: datetime
        
    :param ip: 
    :type ip: ip
    """

    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, blank=True, null=True)
    enabled = models.BooleanField(_('enabled'), default=True)
    category = models.ForeignKey('Category', verbose_name=_('category'), blank=True, null=True)
    author = models.ForeignKey('Author', verbose_name=_('author'), blank=True, null=True)
    tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True)
    quantity = models.IntegerField(_('quantity'), default=0)
    price = models.FloatField(_('price'), default=0.0)
    STATUS_CHOICES = (
        ('not_available', _('Not Available')),
        ('available', _('Available')),
        ('draft', _('Draft')),
        ('withdrawn', _('Withdrawn')),
    )
    status = models.CharField(_('status'), choices=STATUS_CHOICES, max_length=200)
    description = models.TextField(_('description'), blank=True, null=True)
    picture = models.ImageField(_('picture'), blank=True, null=True)
    date_created = models.DateField(_('date_created'), auto_now_add=True)
    date_last_modified = models.DateTimeField(_('date_last_modified'), auto_now=True)
    ip = models.IPAddressField(_('ip'), blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

