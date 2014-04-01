from django.contrib import admin
import example_app.models as m

class Shop(admin.ModelAdmin):
    list_display = ('name', 'post_code')
admin.site.register(m.Shop, Shop)

class FieldInline(admin.TabularInline):
    model = m.Field
    extra = 5

class Farm(admin.ModelAdmin):
    list_display = ('name', 'area')
    inlines = [FieldInline]
admin.site.register(m.Farm, Farm)

class Product(admin.ModelAdmin):
    list_display = ('name', 'color', 'type', 'weight', 'luxury')
admin.site.register(m.Product, Product)

class Basket(admin.ModelAdmin):
    list_display = ('product', 'shop', 'items', 'price')
admin.site.register(m.Basket, Basket)