# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from . import models, forms

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'quantity', 'truncate_body', )

    def truncate_body(self, obj):
        return '%s...' % obj.body[:100]
    truncate_body.short_description = "body"

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(ProductAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Product, ProductAdmin)

