from abc import ABC

from django.contrib import admin, messages
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

from tags.models import TaggedItem
from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 15
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders_placed(self, customer):
        # reverse('admin:app_model_page')
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders=Count('order')
        )


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<5', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<5':
            return queryset.filter(inventory__lt=5)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']
    prepopulated_fields = {
        'slug': ['title']
    }
    search_fields = ['title']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 15
    list_filter = ['collection', 'last_update', InventoryFilter]

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated',
            messages.SUCCESS
        )

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory > 5:
            return 'OK'
        return 'LOW'


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 15
    list_select_related = ['customer']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product', 'product_count']
    list_per_page = 15
    list_select_related = ['featured_product']
    search_fields = ['title']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        # reverse('admin:app_model_page')
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>', url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )
