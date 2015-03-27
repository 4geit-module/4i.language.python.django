# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.contrib.contenttypes import generic
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from . import models, forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', )
    search_fields = ( 'name', )
    ordering = ( 'name', )

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, chance):
        super(CategoryAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', )
    search_fields = ( 'name', )
    ordering = ( 'name', )

    def get_queryset(self, request):
        qs = super(TagAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, chance):
        super(TagAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Tag, TagAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'email', )
    search_fields = ( 'name', )
    ordering = ( 'name', )

    def get_queryset(self, request):
        qs = super(AuthorAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, chance):
        super(AuthorAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Author, AuthorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'slug', 'enabled', 'category', 'author', 'quantity', 'price', 'status', 'description', 'picture', )
    list_filter = ( 'category', 'author', 'tags', 'status', )
    filter_horizontal = ( 'tags', )
    prepopulated_fields = { 'slug': ('name',), }
    search_fields = ( 'name', 'slug', 'category__name', 'author__name', 'tags__name', )
    ordering = ( 'name', 'slug', )

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, chance):
        super(ProductAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Product, ProductAdmin)
