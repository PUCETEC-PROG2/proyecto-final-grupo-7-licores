from django.contrib import admin

# Register your models here.

from .models import Customer, Category, Sale, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass