from django.urls import path
from .views import index, IndexApi

urlpatterns = [
    path('', index),
    path('index_api/', IndexApi.as_view()),
]