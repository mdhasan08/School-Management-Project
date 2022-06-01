from django.shortcuts import render
from .models import About

# Create your views here.
def root(request):
    return render(request, 'index_about.html')

from .serializers import AboutSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class AboutApi(ListAPIView):
    permission_classes = []
    def get(self, request):
        data_val = About.objects.filter().first()
        data_val = AboutSerializer(data_val, many=False).data
        return Response(data_val)