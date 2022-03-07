from django.contrib import admin
from .models import StudentTeacherPost
# Register your models here.
class StudentTeacherPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentTeacherPost,StudentTeacherPostAdmin)