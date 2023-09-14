from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem

class ItemsInOrdersInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'number', 'price',)
    extra = 1

@admin.register(Order)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'is_paid', 'datetime_created',)
    ordering = ('-datetime_created', )
    inlines = [
        ItemsInOrdersInline,
    ]

@admin.register(OrderItem)
class ReviewAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('order', 'product', 'number', 'price',)




