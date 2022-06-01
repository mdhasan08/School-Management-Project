from .models import About
from rest_framework import serializers

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'our_history', 'phone', 'email']