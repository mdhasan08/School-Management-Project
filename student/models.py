from django.db import models
from School_Management.models import SchoolManagementModel
from .string import GENDER_CHOICES,RELIGION_CHOICES,BLOOD_GROUP_CHOICES,STUDENT_CLASS_CHOICES,SECTION_CHOICES,SECTION_CHOICES_DEFAULT,SESSION_CHOICES,SESSION_CHOICES_DEFAULT
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import random
import secrets


# Create your models here.
class Student(SchoolManagementModel):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.PROTECT)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='student/profile_picture',null=True,blank=True)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True,blank=True)
    religion = models.CharField(max_length=10,choices=RELIGION_CHOICES)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=14)
    phone_active = models.BooleanField(default=False)
    guardian_phone = models.CharField(max_length=14,null=True,blank=True)
    guardian_phone_active = models.BooleanField(default=False)
    address = models.TextField(max_length=100)
    blood_group = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES)
    nationality = models.CharField(max_length=15,default='Bangladeshi')
    session = models.CharField(max_length=7,default=SESSION_CHOICES_DEFAULT,choices=SESSION_CHOICES)
    otp = models.CharField(max_length=6,null=True,blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)


    def __str__(self):
        return self.first_name+' '+self.last_name+' (Blood Group : '+self.blood_group+')'+'Phone Active : '+str(self.phone_active)

    def save(self, *args, **kwargs):
        name = self.first_name + self.last_name
        if not self.slug:
            slug = slugify(name)
            student_exist = Student.objects.filter(slug=slug).exists()
            if student_exist:
                hexa = secrets.token_hex(6)
                self.slug = slug + "-Xyb09b-" + hexa
            else:
                self.slug = slug

            super(Student, self).save(*args, **kwargs)
        else:
            super(Student, self).save(*args, **kwargs)


class ClassInformation(SchoolManagementModel):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="Class_Information")
    student_class = models.CharField(max_length=3, null=False, blank=False, choices=STUDENT_CLASS_CHOICES)
    class_roll = models.PositiveIntegerField()
    section = models.CharField(max_length=1, choices=SECTION_CHOICES, default=SECTION_CHOICES_DEFAULT)
    admission_date = models.DateField()



    def __str__(self):
        return self.student.first_name+' '+self.student.last_name+'-roll-'+str(self.class_roll)+'-class-'+str(self.class_roll)

class Subject(SchoolManagementModel):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="Student_Subject")
    subject = models.CharField(max_length=50)


    def __str__(self):
        return self.student.first_name+' '+self.student.last_name+' ('+self.subject+')'



from django.db.models.signals import pre_save,post_save
from School_Management.models import history_time_info
pre_save.connect(history_time_info,sender=Student)
pre_save.connect(history_time_info,sender=ClassInformation)
pre_save.connect(history_time_info,sender=Subject)