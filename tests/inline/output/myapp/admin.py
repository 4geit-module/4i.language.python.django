# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from . import models, forms

class ProductTagInline(admin.TabularInline):
    model = models.ProductTag
    extra = 1

class ProductKeywordInline(admin.StackedInline):
    model = models.ProductKeyword
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', )
    inlines = [ ProductTagInline, ProductKeywordInline, ]

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(ProductAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Product, ProductAdmin)

