from atexit import register
from django.contrib import admin
from .models import Student, ClassInformation, Subject
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, AllValuesFieldListFilter, ChoicesFieldListFilter, RelatedOnlyFieldListFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # queryset = Student.objects.filter(is_archived=True).all()
        queryset = Student.objects.filter().order_by('id')
        return queryset
    fields = [
        ('first_name', 'last_name', 'user', 'slug'),
        ('father_name', 'mother_name'),
        ('profile_picture'),
        ('gender', 'religion', 'blood_group'),
        ('birth_date'),
        ('address'),
        ('email', 'phone', 'phone_active'),
        ('guardian_phone', 'guardian_phone_active'),
        ('is_archived'),
        ('nationality', 'session')
    ]
    readonly_fields = ["slug"]
    search_fields = ['first_name__icontains', 'phone__icontains']
    list_filter = (
        ('gender', DropdownFilter),
        ('blood_group', DropdownFilter),
        ('religion', DropdownFilter),
        ('modified_at', DateRangeFilter),
        ('created_at', DateTimeRangeFilter),
        ('first_name', AllValuesFieldListFilter),
        ('email', ChoicesFieldListFilter),
    )
    list_display = ['id', 'first_name', 'last_name','user','otp', 'email', 'phone', 'created_at', 'modified_at', 'archived_at']
    list_per_page = 3


admin.site.register(Student, StudentAdmin)


class ClassInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(ClassInformation, ClassInformationAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_filter = (
        ('student', RelatedDropdownFilter),
        ('subject', DropdownFilter),
    )
    fields = ['student','subject','is_archived']


admin.site.register(Subject, SubjectAdmin)