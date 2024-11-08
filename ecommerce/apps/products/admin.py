from django.contrib import admin

from apps.products.models import Material, Category, Product


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
        'stock',
        'category',
        'get_materials',
        'modified',
        'created',
    ]
    list_filter = [
        'category',
        'materials',
    ]
    search_fields = ['name']
    autocomplete_fields = [
        'category',
        'materials',
    ]
    filter_horizontal = [
        'materials',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]

    def get_materials(self, obj):
        return ', '.join([m.name for m in obj.materials.all()])

    get_materials.short_description = 'Materials'
