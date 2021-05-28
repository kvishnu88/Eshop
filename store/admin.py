from django.contrib import admin
from store.models import Product, Category, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','description','category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']
