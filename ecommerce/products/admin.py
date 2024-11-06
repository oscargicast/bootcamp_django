from django.contrib import admin

from products.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
