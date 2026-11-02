
from django.contrib import admin
from .models import Product, Box


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'length', 'width',
        'height', 'weight', 'is_active'
    )
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'internal_length',
        'internal_width', 'internal_height',
        'max_weight', 'cost', 'is_active'
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
