from django.contrib import admin
from food.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
