from django.contrib import admin
from .models import Customer
from .models import StoreOwner
from .models import ProductCompany
# Register your models here.
admin.site.register(Customer)
admin.site.register(StoreOwner)
admin.site.register(ProductCompany)