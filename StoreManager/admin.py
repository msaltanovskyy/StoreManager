from django.contrib import admin
from .models import Product, Store, Category, Warehouse, Supplier

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'store', 'category')
    readonly_fields = ('created_at', 'updated_at')  # Сделать поля только для чтения
    search_fields = ('name', 'store__name', 'category__name')
    list_filter = ('category', 'store', 'created_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'price', 'store', 'category')
        }),
        ('Запасы и даты', {
            'fields': ('stock_quantity', 'updated_at'),
            'classes': ('collapse',)  # Скрыть этот раздел по умолчанию
        }),
    )

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'created_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'manager', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'contact_name', 'email')
    list_filter = ('created_at',)
