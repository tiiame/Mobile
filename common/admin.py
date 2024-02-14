from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_avaible', 'guarantee', 'delivery', 'pickup', 'life_time','made_by', 'category',)
    list_editable = ('is_avaible',)
    list_filter = ('is_avaible',)

@admin.register(Productimage)
class ProductimageAdmin(admin.ModelAdmin):
    list_display = ('product', 'color', 'image_1', 'image_2', 'image_3', 'price',)


@admin.register(Productprice)
class ProductpriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price','memory',)


@admin.register(Productinfo)
class ProductinfoAdmin(admin.ModelAdmin):
    list_display = ('product', 'key',)


@admin.register(ProductinfoType)
class ProductinfoTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'Price', 'time', 'product',)

@admin.register(ServiceApplication)
class ServiceApplicationAdmin(admin.ModelAdmin):
    list_display = ('sevice', 'full_name', 'phone_number',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('image', 'full_name', 'position', 'type',)

