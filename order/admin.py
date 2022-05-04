from django.contrib import admin
from .models import *


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'paid', 'postal_code', 'created_at', 'get_total_cost']
    list_display_links = ['id', 'created_at']
    list_filter = ['paid', 'city']
    inlines = [OrderItemInLine]

    def get_total_cost(self, order):
        return order.get_total_cost()


admin.site.register(Order, OrderAdmin)
