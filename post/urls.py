from django.urls import path
from .views import post_index, PostCreateApi, PostListApi, PostLike, post_list

urlpatterns=[
    path('', post_index),
    path('post_list/', post_list),
    #api
    path('post_create_api/', PostCreateApi.as_view()),
    path('post_like_api/<str:id>/', PostLike.as_view()),
    path('post_list_api/', PostListApi.as_view()),
]