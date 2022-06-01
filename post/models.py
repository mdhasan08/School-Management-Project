from student.models import Student
from teacher.models import Teacher
from django.db import models
from School_Management.models import SchoolManagementModel
from django.contrib.auth.models import User

# Create your models here.
class Post(SchoolManagementModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=True, blank=True)
    picture = models.ImageField(upload_to="post/picture", null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return str(self.id)+'  '+self.text


class Like(SchoolManagementModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="user_post")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

from django.db.models.signals import pre_save, post_save
from School_Management.models import history_time_info
pre_save.connect(history_time_info, sender=Post)
pre_save.connect(history_time_info, sender=Like)