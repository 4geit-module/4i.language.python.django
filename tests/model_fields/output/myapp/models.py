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
    class Meta:
        verbose_name_plural = _('categories')
    
    name = models.CharField(_('name'), max_length=200, unique=True)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Tag(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True)

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Author(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True)
    email = models.EmailField(_('email'), blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

class Product(models.Model):
    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, blank=True, null=True)
    enabled = models.BooleanField(_('enabled'), default=True)
    category = models.ForeignKey('Category', verbose_name=_('category'), blank=True, null=True)
    author = models.ForeignKey('Author', verbose_name=_('author'), blank=True, null=True)
    tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True, null=True)
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

