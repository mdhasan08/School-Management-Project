from django.db import models
from School_Management.models import SchoolManagementModel

# Create your models here.
class About(SchoolManagementModel):
    our_history = models.CharField(max_length=10000)
    phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)