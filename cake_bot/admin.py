from django.contrib import admin

from .models import Cake, Order, Customer, Product, \
     Product_parameters, Product_properties


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'weight')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'tg_username', 'first_name',
                    'last_name', 'phone_number', 'GDPR_status', 'home_address')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')

@admin.register(Product_properties)
class Product_propertiesAdmin(admin.ModelAdmin):
    list_display = ('product', 'property_name')

@admin.register(Product_parameters)
class Product_parametersAdmin(admin.ModelAdmin):
    list_display = ('product_property', 'parameter_name', 'parameter_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_details', 'cake_name', 'order_price', 'order_status')
    list_filter = ['order_status', 'order_type']
    list_editable = ('order_status', )
