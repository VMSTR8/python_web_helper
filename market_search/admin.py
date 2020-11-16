from django.contrib import admin
from .models import Items, Categories, Stores

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'in_stock', 'link', 'price', 'store', 'category')
    list_display_links = ('item_name', )
    search_fields = ('item_name', )
    list_filter = ('in_stock', 'category')
    exclude = ('search_vector', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class StoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'discount', 'logo')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(Items, ItemAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Stores, StoresAdmin)
