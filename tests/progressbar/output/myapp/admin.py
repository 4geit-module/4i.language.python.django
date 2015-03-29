# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.contrib.contenttypes import generic
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from . import models, forms

class ProductAdmin(admin.ModelAdmin):
    exclude = ( 'progress', )
    list_display = ( 'id', 'name', 'quantity', 'status', 'progressbar', )
    list_filter = ( 'status', )
    search_fields = ( 'status', )
    ordering = ( '-progress', )

    def progressbar(self, obj):
        progress_text = obj.progress if obj.progress else 0
        progress = int(round(obj.progress/5)) if obj.progress else 0
        remain_progress = 20-progress
        return '[%s%s] %d%%' % (progress*'#', remain_progress*'=', progress_text)
    progressbar.short_description = "progressbar"
    progressbar.admin_order_field = "progress"

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(ProductAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Product, ProductAdmin)

