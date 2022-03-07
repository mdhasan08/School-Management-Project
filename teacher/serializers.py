from rest_framework import serializers
from .models import Teacher

class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','profile_picture','salary','father_name','mother_name','gender','religion','blood_group','phone','fax','email','birth_date','joining_date','retirement_date','is_archived','address','student']

class TeacherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','profile_picture','salary','father_name','mother_name','gender','religion','blood_group','phone','fax','email','birth_date','joining_date','retirement_date','is_archived','address','student']