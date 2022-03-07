from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .serilizers import PostSerializer
from .models import StudentTeacherPost
from rest_framework.response import Response

# Create your views here.
def post_index(request):
    return render(request,'post_index.html')


class PostApi(CreateAPIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        post_data = request.data
        student_techer_post = StudentTeacherPost()
        student_techer_post.post = post_data['post']
        student_techer_post.post_picture = request.FILES['post_picture'] 
        student_techer_post.save()
        return Response("Success")


class PostShowApi(ListAPIView):
    permission_classes=[]
    def get(self, request):
        data_val = StudentTeacherPost.objects.filter().all()
        data_val = PostSerializer(data_val, many=True).data
        return Response(data_val)
        