
from django.contrib import admin
from .models import Product ,Category # Or any other model

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category_id','category_name')
    list_filter = ['id','category', 'name']
    search_fields = ['id','category__name', 'name']

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Category Name'  # Custom column title
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','slug')
    list_filter = ['id', 'name']
    search_fields = ['id','name']
admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)