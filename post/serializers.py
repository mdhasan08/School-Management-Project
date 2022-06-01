from rest_framework import serializers
from .models import Post, Like
from student.models import Student
from teacher.models import Teacher

class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'profile_picture']

class TeacherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'profile_picture']

class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user']

class PostListSerializer(serializers.ModelSerializer):
    total = serializers.CharField()
    user_post = LikeListSerializer(many=True)
    student = StudentDataSerializer(many=False)
    teacher = TeacherDataSerializer(many=False)
    class Meta:
        model = Post
        fields = ['id', 'student', 'teacher', 'text', 'picture', 'total', 'user_post']

