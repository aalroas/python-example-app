from django.contrib import admin
from .models import Product
from .models import Customer

admin.site.register([
    Product,
    Customer
    ])