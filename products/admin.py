from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)



class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_field = ('name', 'description')
    list_filter = ('price',)

admin.site.register(Item, MenuAdmin)


