from django.contrib import admin
from .models import Store
from .models import Certification
from .models import Review
# Register your models here.

admin.site.register(Store)
admin.site.register(Certification)
admin.site.register(Review)