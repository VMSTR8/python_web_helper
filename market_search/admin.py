from django.contrib import admin
from .models import Items

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'in_stock', 'link', 'store_name')


admin.site.register(Items, ItemAdmin)
