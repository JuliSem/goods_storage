from django.contrib import admin

from goods.models import Good, Type


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'type', 'quantity',
        'price', 'barcode', 'update_date'
    )
    list_filter = ('name', 'type')
    search_fields = ('name', 'barcode')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', )
