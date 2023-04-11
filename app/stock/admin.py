from django.contrib import admin

from .models import Category, ChangeItem, Item

admin.site.register(Category)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "supplier",
    ]


@admin.register(ChangeItem)
class ChangeItemAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "qty",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    ]
