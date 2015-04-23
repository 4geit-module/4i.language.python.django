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

    def number_of_product(self, obj):
        return obj.product_count
    number_of_product.short_description = "# product"
    number_of_product.admin_order_field = "product_count"

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        qs = qs.annotate(product_count=Count('product')).order_by('-product_count')
        return qs

    def save_related(self, request, form, formsets, change):
        super(CategoryAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'quantity', 'status', 'number_of_categories', )
    list_filter = ( 'status', 'categories', )
    filter_horizontal = ( 'categories', )
    search_fields = ( 'status', 'categories__name', )

    def number_of_categories(self, obj):
        return obj.categories_count
    number_of_categories.short_description = "# categories"
    number_of_categories.admin_order_field = "categories_count"

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        qs = qs.annotate(categories_count=Count('categories')).order_by('-categories_count')
        return qs

    def save_related(self, request, form, formsets, change):
        super(ProductAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()

admin.site.register(models.Product, ProductAdmin)

