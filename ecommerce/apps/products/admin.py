from django.contrib import admin

from apps.products.models import (
    Material,
    Thickness,
    Category,
    Product,
    ProductLine,
)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'modified',
        'created',
    ]
    search_fields = ['name']
    readonly_fields = [
        'created',
        'modified',
    ]


@admin.register(Thickness)
class ThicknessAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'material',
        'value',
        'modified',
        'created',
    ]
    list_filter = [
        'material',
    ]
    search_fields = [
        'material__name',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'modified',
        'created',
    ]
    search_fields = ['name']
    readonly_fields = [
        'created',
        'modified',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'category',
        'material',
        'modified',
        'created',
    ]
    list_filter = [
        'category',
        'material',
    ]
    search_fields = ['name']
    autocomplete_fields = [
        'category',
        'material',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order',
        'product',
        'units',
        'unit_price',
        'total_price',
        'created',
    ]
    list_filter = [
        'product',
        'order__status',
    ]
    search_fields = [
        'product__name',
        'order__user__email',
        'order__user__first_name',
        'order__user__last_name',
        'order__user__mobile',
    ]
    autocomplete_fields = [
        'order',
        'product',
    ]
    readonly_fields = [
        'unit_price',
        'total_price',
        'created',
        'modified',
    ]
