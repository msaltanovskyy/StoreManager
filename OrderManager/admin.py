from django.contrib import admin
from .models import Order, OrderItem, DeliveryMethod, Discount, Payment, Coupon


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'shipping_address', 'payment_method')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fields = ('user', 'status', 'shipping_address', 'payment_method', 'note', 'total_amount')  # Добавить total_amount


    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'total_price')
    search_fields = ('product__name', 'order__id')
    list_filter = ('order__status',)


@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'estimated_time')
    search_fields = ('name',)
    list_filter = ('cost',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_type', 'value', 'start_date', 'end_date', 'active')
    search_fields = ('name',)
    list_filter = ('discount_type', 'active', 'start_date', 'end_date')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'payment_status', 'payment_date', 'transaction_id')
    search_fields = ('order__id', 'transaction_id', 'payment_method')
    list_filter = ('payment_status', 'payment_method', 'payment_date')


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active', 'usage_limit')
    search_fields = ('code',)
    list_filter = ('active', 'valid_from', 'valid_to')
