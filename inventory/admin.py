from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
