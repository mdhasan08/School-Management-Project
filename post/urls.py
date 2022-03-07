from django.urls import path
from .views import post_index,PostApi,PostShowApi

urlpatterns=[
    path('',post_index),
    path('post_api/',PostApi.as_view()),
    path('post_show_api/',PostShowApi.as_view()),
]