from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import PostListSerializer, LikeListSerializer
from .models import Post
from rest_framework.response import Response
from django.db.models import Prefetch

# Create your views here.
def post_index(request):
    return render(request, 'post_index.html')


from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from student.models import Student
from teacher.models import Teacher


class PostCreateApi(CreateAPIView):
    permission_classes = [IsUser]
    def post(self, request, *args, **kwargs):
        # user = User.objects.get(id=request.user.id)
        # user = User.objects.filter(id=request.user.id).first()
        post = Post()
        student = Student.objects.filter(user=request.user).first()
        if student:
            post.student = student
        else:
            teacher = Teacher.objects.filter(user=request.user).first()
            post.teacher = teacher
        post.user = request.user
        if 'text' not in request.data and request.data['text'] == '':
            result = {}
            result["Status"] = HTTP_400_BAD_REQUEST
            result["Message"] = "Please provide a post"
            return Response(result)
        else:
            post.text = request.data['text']
        post.picture = request.FILES['picture'] 
        post.save()
        result = {}
        result["Status"] = HTTP_200_OK
        result["Messase"] = "Post Done"
        return Response(result)


from .models import Like

class PostLike(CreateAPIView):
    permission_classes = [IsUser]
    def post(self, request, id):
        user = request.user
        result = {}
        like = Like.objects.filter(user=user, post__id=id).exists()
        if like:
            result["Status"] = HTTP_200_OK
            result["Message"] = "Already liked"
            return Response(result)
        else: 
            post = Post.objects.filter(id=id).first()
            like = Like()
            like.user = user
            like.post = post
            like.save()
            result["Status"] = HTTP_200_OK
            result["Message"] = "Like done"
            return Response(result)

from django.db.models import Count

class PostListApi(ListAPIView):
    permission_classes = [IsUser]
    def get(self, request):
        post_list = Post.objects.filter().prefetch_related(Prefetch("user_post", Like.objects.filter(user=request.user).all())).annotate(total=Count("user_post")).all()
        post_list = PostListSerializer(post_list, many=True).data
        return Response(post_list)
        
def post_list(request):
    return render(request, 'post_list.html')

