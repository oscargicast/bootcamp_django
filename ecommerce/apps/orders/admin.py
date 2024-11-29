from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'discount',
        'total_price',
        'status',
        'created',
    ]
    list_filter = [
        'status',
    ]
    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name',
        'user__mobile',
    ]
    autocomplete_fields = [
        'user',
    ]
    readonly_fields = [
        'created',
        'modified',
        'total_price',
    ]
