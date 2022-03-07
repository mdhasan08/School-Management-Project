from django.contrib import admin
from .models import Teacher,TeacherEducaionalQualification,TeacherExperience

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset = Teacher.objects.filter(is_archived=False).order_by('id')
        return queryset
    filter_horizontal = ('student',)
    fields = [('first_name','last_name'),'profile_picture','salary',('father_name','mother_name'),('gender','religion','blood_group'),('phone','fax','email'),('birth_date','joining_date','retirement_date'),'is_archived','address','student']
    search_fields = ['first_name__icontains','phone__icontains']
    list_display = ['id','first_name','last_name','birth_date','email','phone','salary','is_archived','created_at','modified_at','archived_at']
    list_per_page = 10
    
admin.site.register(Teacher,TeacherAdmin)


class TeacherEducaionalQualificationAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherEducaionalQualification,TeacherEducaionalQualificationAdmin)



class TeacherExperienceAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExperience,TeacherExperienceAdmin)