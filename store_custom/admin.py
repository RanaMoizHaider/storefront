from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline


class TagInline(GenericTabularInline):
    # autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 1


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)