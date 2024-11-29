from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'file',
        'order__user',
        'units',
        'thickness',
        'fold_number',
        'material',
        'units',
        'total_price',
        'created',
    ]
    list_filter = [
        'material',
        'order__status',
    ]
    search_fields = [
        'order__user__email',
        'order__user__first_name',
        'order__user__last_name',
        'order__user__mobile',
    ]
    autocomplete_fields = [
        'material',
        'order',
    ]
    readonly_fields = [
        'total_price',
        'created',
        'modified',
    ]
