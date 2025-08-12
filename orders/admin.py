from django.contrib import admin

from .models omport *

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'order_status', 'created_at')
    search_fields = ('customer_username', 'order_status')
    list_filter = ('order_status', 'created_at')
    filter_horizontal = ('order_items',)


admin.site.Register()
