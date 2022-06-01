from ipaddress import ip_address
from django.urls import path
from .views import IPAddress


urlpatterns = [
    path('',IPAddress.as_view()),
]