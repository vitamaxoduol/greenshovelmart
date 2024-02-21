from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.products import Products

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Products)
