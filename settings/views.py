from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
# Create your views here.

class IPAddress(ListAPIView):
    permission_classes = []
    def get(self, request):
        print(request.META)
        print(request.META.get('REMOTE_ADDR'))
        return Response(request.META.get('REMOTE_ADDR'))