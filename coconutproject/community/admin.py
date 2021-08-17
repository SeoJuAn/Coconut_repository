from django.contrib import admin

from .models import Community
from .models import Photo
# Register your models here.

#admin.site.register(Community)

# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo

class CommunityAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

admin.site.register(Community,CommunityAdmin)

