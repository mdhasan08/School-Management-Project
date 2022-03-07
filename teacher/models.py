from importlib.resources import path
from django.db import models
from student.models import Student
from School_Management.models import SchoolManagementModel
from .string import GENDER_CHOICES,GENDER_CHOICES_DEFAULT,BLOOD_GROUP_CHOICES,RELIGION_CHOICES,RELIGION_CHOICES_DEFAULT,POINT_OUT_OF_CHOICES,DEGREE_CHOICES
# Create your models here.
class Teacher(SchoolManagementModel):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to="teacher/profile_picture",null=True,blank=True)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default=GENDER_CHOICES_DEFAULT)
    religion = models.CharField(max_length=8,choices=RELIGION_CHOICES,default=RELIGION_CHOICES_DEFAULT)
    phone = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=30)
    fax = models.CharField(max_length=14, null=True,blank=True)
    blood_group = models.CharField(max_length=3,null=False,blank=False,choices=BLOOD_GROUP_CHOICES)
    birth_date = models.DateField()
    joining_date = models.DateField()
    retirement_date = models.DateField()
    address = models.TextField(max_length=100,null=False,blank=False)
    salary = models.PositiveIntegerField()
    student = models.ManyToManyField(Student, blank=True)
    
    

    def __str__(self):
        return self.first_name+' '+self.last_name+' '+' - ('+self.blood_group+')'



    
class TeacherEducaionalQualification(SchoolManagementModel):
    teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT,related_name="Teacher_Educaional_Qualification")
    degree = models.CharField(max_length=7,choices=DEGREE_CHOICES)
    institue = models.CharField(max_length=30)
    passing_year = models.PositiveIntegerField()
    board = models.CharField(max_length=8)
    grade_point = models.FloatField()
    point_out_of = models.CharField(max_length=4,choices=POINT_OUT_OF_CHOICES)


    def __str__(self):
        return self.teacher.first_name+' '+self.teacher.last_name+' ('+self.degree+')'


class TeacherExperience(SchoolManagementModel):
    teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT,related_name="Teacher_Experience")
    institute_name = models.CharField(max_length=20)
    job_designation = models.CharField(max_length=20)
    joining_year = models.PositiveIntegerField()
    job_duration = models.CharField(max_length=8)

    def __str__(self):
        return self.teacher.first_name+' '+self.teacher.last_name+' ('+self.job_designation+')'



from django.db.models.signals import pre_save,post_save
from School_Management.models import history_time_info
pre_save.connect(history_time_info,sender=Teacher)
pre_save.connect(history_time_info,sender=TeacherEducaionalQualification)
pre_save.connect(history_time_info,sender=TeacherExperience)

