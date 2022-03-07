from distutils.command.upload import upload
from django.db import models

# Create your models here.
class StudentTeacherPost(models.Model):
    post_picture=models.ImageField(upload_to="post/post_picture")
    post=models.TextField()


    def __str__(self):
        return str(self.id)+'  '+self.post