from django.contrib import admin
from .models import About
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    fields = [
        'our_history',
        'phone',
        'email'
    ]
    list_display = [
        'id',
        'phone',
        'email'
    ]
    search_filed = ['phone__icontains']
    list_per_page = 10
admin.site.register(About, AboutAdmin)