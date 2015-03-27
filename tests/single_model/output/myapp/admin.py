# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.contrib.contenttypes import generic
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from . import models, forms

class MyModelAdmin(admin.ModelAdmin):
    list_display = ( 'id', )

    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, chance):
        super(MyModelAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.MyModel, MyModelAdmin)
