from rest_framework import serializers
from .models import StudentTeacherPost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTeacherPost
        fields = ['post','post_picture']