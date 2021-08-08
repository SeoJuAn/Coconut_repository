from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline
from .models import Store
from .models import Certification
from .models import Review
from .models import Photo
from .models import Photo_review

# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo

class StoreAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

class PhotoInline_review(admin.TabularInline):
    model = Photo_review
    
class ReviewAdmin(admin.ModelAdmin):
    inlines = [PhotoInline_review,]

admin.site.register(Store,StoreAdmin)
admin.site.register(Certification)
admin.site.register(Review,ReviewAdmin)