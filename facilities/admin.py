from django.contrib import admin
from .models import Facilities


class FacilitiesAdmin(admin.ModelAdmin):
    # list_display=['title','description']
    search_fields = ['title__icontains']
admin.site.register(Facilities, FacilitiesAdmin)