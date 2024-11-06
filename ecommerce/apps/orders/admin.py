from django.contrib import admin

from .models import Order, OrderLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'total_discount',
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
        'total_discount',
        'total_price',
    ]


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order',
        'product',
        'units',
        'unit_price',
        'discount',
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
        'total_price',
        'created',
        'modified',
    ]
