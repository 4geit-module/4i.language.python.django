# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from . import models, forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'number_of_product', )
    search_fields = ( 'name', )
    ordering = ( 'name', )

    def number_of_product(self, obj):
        return obj.product_set.count()
    number_of_product.short_description = "# product"

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(CategoryAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'number_of_product', )
    search_fields = ( 'name', )
    ordering = ( 'name', )

    def number_of_product(self, obj):
        return obj.product_set.count()
    number_of_product.short_description = "# product"

    def get_queryset(self, request):
        qs = super(TagAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(TagAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Tag, TagAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'email', 'number_of_product', )
    search_fields = ( 'name', )
    ordering = ( 'name', )

    def number_of_product(self, obj):
        return obj.product_set.count()
    number_of_product.short_description = "# product"

    def get_queryset(self, request):
        qs = super(AuthorAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(AuthorAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Author, AuthorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'slug', 'enabled', 'category', 'author', 'quantity', 'price', 'status', 'description', 'picture', 'number_of_tags', )
    list_filter = ( 'category', 'author', 'tags', 'status', )
    filter_horizontal = ( 'tags', )
    prepopulated_fields = { 'slug': ('name',), }
    search_fields = ( 'name', 'slug', 'category__name', 'author__name', 'tags__name', )
    ordering = ( 'name', 'slug', )

    def number_of_tags(self, obj):
        return obj.tags.count()
    number_of_tags.short_description = "# tags"

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return qs

    def save_related(self, request, form, formsets, change):
        super(ProductAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Product, ProductAdmin)

