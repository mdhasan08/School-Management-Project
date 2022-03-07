from dataclasses import field
from inspect import classify_class_attrs
from multiprocessing import managers
from rest_framework import serializers
from .models import Student,ClassInformation,Subject


# class StudentListSerilazers(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id','first_name', 'last_name','user', 'father_name', 'mother_name', 'profile_picture', 'gender', 'religion', 'blood_group', 'birth_date', 'email', 'phone', 'phone_active', 'guardian_phone', 'guardian_phone_active', 'is_archived', 'nationality', 'session','Class_Information']


class StudentClassInformation(serializers.ModelSerializer):
    class Meta:
        model = ClassInformation
        fields = ['id','student_class','class_roll','section','admission_date']


class StudentSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject']


class StudentListSerializers(serializers.ModelSerializer):
    Class_Information = StudentClassInformation(many = True)
    Student_Subject = StudentSubjectSerializers(many = True)
    class Meta:
        model = Student
        fields = ['id','first_name', 'last_name','user', 'father_name', 'mother_name', 'profile_picture', 'gender', 'religion', 'blood_group', 'birth_date', 'email', 'phone', 'phone_active', 'guardian_phone', 'guardian_phone_active', 'is_archived', 'nationality', 'session','Class_Information','Student_Subject']