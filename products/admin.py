from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Review

class ReviewInProductInline(admin.TabularInline):
    model = Review
    fields = ('author', 'body', 'stars', 'active',)
    extra = 1

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_created', 'active',)
    ordering = ('-datetime_created', )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ReviewInProductInline,
    ]

@admin.register(Review)
class ReviewAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('author', 'product', 'datetime', 'stars', 'active',)
    ordering = ('-datetime', )




