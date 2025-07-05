from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    def get_friendly_name(self, obj):
        return obj.get_friendly_name()

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
