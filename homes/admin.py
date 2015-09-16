from django.contrib import admin
from homes.models import Customer, Home


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('address','city', 'state', 'zipcode', 'price', 'sqft',
                    'bedrooms', 'bathrooms', 'lot_size', 'price_per_sqft',
                    'year_built', 'img')