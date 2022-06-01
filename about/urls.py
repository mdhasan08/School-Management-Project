from django.urls import path
from .views import root, AboutApi

urlpatterns = [
    path('', root),
    path('about_api/', AboutApi.as_view()),
]