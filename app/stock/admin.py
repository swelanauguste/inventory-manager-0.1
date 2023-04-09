from django.contrib import admin

from .models import Category, RemoveItem, Item, ReceiveItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "supplier",
        "price",
        "get_item_total_count",
        "get_total_cost",
    ]


admin.site.register(RemoveItem)
admin.site.register(Category)
admin.site.register(ReceiveItem)
