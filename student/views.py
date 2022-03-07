from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,ClassInformation
from django.db.models import Prefetch
# Create your views here.
def root1(request):
    text = "Welcome students"
    return HttpResponse(text)

    
from django.db.models import Q
def root(request):
    # data = Student.objects.filter().all()
    # data = Student.objects.filter().last()
    # data = Student.objects.filter().first()
    # data = Student.objects.filter(gender='Female')
    # data = Student.objects.filter().exclude(first_name='Ashik')
    data = Student.objects.filter(Q(first_name='Ashik') | Q(first_name='Rahim'))
    
    return render(request,'student.html',{'val':data}) 

def root1(request,sc):
    data = ClassInformation.objects.filter().prefetch_related("Class_Information")#.order_by('admission_date')
    student_data = data.filter(student_class=sc)
    # total_count = data.count()
    total_count = student_data.count()
    # data = Student.objects.filter().all()
    # data = Student.objects.filter().last()
    # data = Student.objects.filter().first()
    # data = Student.objects.filter(gender='Female')
    # data = ClassInformation.objects.filter(student__first_name='Adnan').first()
    # data = ClassInformation.objects.filter(student__first_name='Adnan')
    # print(data.student.first_name)
    return render(request,'student.html',{'value':student_data,'total_count':total_count}) 


def header(request):
    return render(request,'layout/header.html')


def student_index(request):
    return render(request,'student_index.html')


def student_list(request):
    data_val = Student.objects.filter().all().order_by('id')
    from School_Management import settings
    media_url = settings.MEDIA_URL
    return render(request,'student_list.html',{'data':data_val,'media_url':media_url})


def student_details(request,id):
    data_val = Student.objects.filter(id=id).first()
    data_val1 = ClassInformation.objects.filter(student__id=id).last()
    from School_Management import settings
    media_url = settings.MEDIA_URL
    return render(request, 'student_details.html', {'data': data_val, 'media_url': media_url, 'data1': data_val1})


from django.contrib.auth.models import User, Group
def is_student(user):
    user = User.objects.filter(id=user).first()
    return user.groups.filter(name='Student').exists()


from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import StudentListSerializers
from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_student(request.user.id))

# class StudentListApi(ListAPIView):
#     permission_classes = [IsStudent]
#     def get(self,request):
#         data_val = Student.objects.filter().all()
#         print(data_val)
#         data_val = StudentListSerilazers(data_val, many=True).data
#         return Response(data_val)


class StudentListApi(ListAPIView):
    permission_classes = []
    def get(self, request):
        data_val = Student.objects.filter().prefetch_related("Class_Information","Student_Subject").all()
        data_val = StudentListSerializers(data_val,many = True).data
        return Response(data_val)


def sign_up(request):
    return render(request,'student_sign_up.html')

from rest_framework.generics import CreateAPIView
from rest_framework.utils import json
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import random

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(to, subject, body):
    smtp_server='smtp.gmail.com'
    smtp_port='465'
    sender_email='mynulhasan642@gmail.com'
    sender_password='@mynulhasan@642@'
    server = None
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()  # Can be omitted
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject


        html = """\
        <html>
            <head></head>
            <body>
        """
        html += body.replace('\r\n', '<br />\r\n')
        """
            </body>
        </html>
        """
        msg.attach(MIMEText(html,'html'))
        server.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg = msg.as_string())
        print("Mail Send")
    except Exception as ex:
        print(str(ex))
    finally:
        if server != None:
            server.quit()



class SignUpApi(CreateAPIView):
    permission_classes=[]
    def post(self,request):
        result={}
        try:
            data = json.loads(request.body)
            if 'first_name' not in data or data['first_name']=='':
                result["Message"]="First Name required"
                result["Error"]="First Name"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'last_name' not in data or data['last_name']=='':
                result["Message"]="Last Name required"
                result["Error"]="Last Name"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'gender' not in data or data['gender']=='':
                result["Message"]="Gender required"
                result["Error"]="Gender"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'birth_date' not in data or data['birth_date']=='':
                result["Message"]="Birth Date required"
                result["Error"]="Birth Date"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'phone' not in data or data['phone']=='':
                result["Message"]="Phone required"
                result["Error"]="Phone"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'email' not in data or data['email']=='':
                result["Message"]="Email required"
                result["Error"]="Email"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'password' not in data or data['password']=='':
                result["Message"]="Password required"
                result["Error"]="Password"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()

            if not user:
                user = User()
                user.username = data['email']
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.email = data['email']
                user.password = make_password(data['password'])
                user.is_active = False
                user.save()
                random_number = random.randint(100000,900000)
                student = Student()
                student.first_name = data['first_name']
                student.last_name = data['last_name']
                student.email = data['email']
                student.otp = random_number
                student.user = user
                student.save()
                send_email(data['email'], 'Student sign up OTP','Your OTP is: ' + str(random_number))
                result={}
                result["status"]=HTTP_200_OK
                result["Message"]="Success"
                result["Email"]=data['email']
                return Response(result)

            elif user:
                if user.is_active == True:
                    result={}
                    result['Message']='Your account is already active'
                    result['status']=HTTP_200_OK
                    return Response(result)
                else:
                    user.first_name = data['first_name']
                    user.last_name = data['last_name']  
                    user.password = make_password(data['password'])
                    user.is_active = False
                    user.save()
                    random_number = random.randint(100000,900000)
                    student = Student.objects.filter(user=user).first()
                    student.first_name = data['first_name']
                    student.last_name = data['last_name']
                    student.otp = random_number
                    student.save()
                    send_email(data['email'], 'Student sign up OTP','Your OTP is: ' + str(random_number))
        except:
            return Response("False")



import json
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK
from django.contrib.auth.models import User
class OtpCheckApi(ListAPIView):
    persmission_class=[]
    def put(self,request):
        result={}
        try:
            data=json.loads(request.body)
            print(data)
            if 'email' not in data or data['email']=='':
                result["Message"]="Email required"
                result["Error"]="Email"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            if 'otp' not in data or data['otp']=='':
                result["Message"]="OTP required"
                result["Error"]="OTP"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            user= User.objects.filter(username=data['email']).first()
            if not user:
                result["Message"]="First you have to create account"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            elif user.is_active:
                result["Message"]="You already created an account"
                return Response(result,status=HTTP_400_BAD_REQUEST)

            else:
                student = Student.objects.filter(user=user).first()
                if student.otp == data['otp']:
                    user.is_active = True
                    group = Group.objects.filter(name = 'Student').first()
                    user.groups.add(group)
                    user.save()
                    student.otp=''
                    student.save()
                    result={}
                    result["Message"]="Success"
                    result["Status"]=HTTP_200_OK
                    return Response(result)
                else:
                    result={}
                    result["Status"]=HTTP_400_BAD_REQUEST
                    result["Message"]='OTP did not match!'
                    result["Error"]="OTP"
                    return Response(result)

        except Exception as ex:
            result={}
            result["Message"]=str(ex)
            return Response(result)



from rest_framework.generics import ListAPIView
from rest_framework.utils import json
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
class StudentSignInApi(ListAPIView):
    permission_classes=[]
    def post(self, request):
        result={}
        try:
            data = json.loads(request.body)
            print(data)
            if 'email' not in data or data['email']=='':
                result["Message"]="Email required"
                result["Error"]="Email"
                return Response(result,HTTP_400_BAD_REQUEST)

            if 'password' not in data or data['password']=='':
                result["Message"]="Password required"
                result["Error"]="Password"
                return Response(result,HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            print(user)
            if not user:
                result["Message"]="Please first create an account"
                return Response(result,status=HTTP_401_UNAUTHORIZED)

            elif not user.is_active:
                result["Message"]="First you have to active your account"
                return Response(result,status=HTTP_400_BAD_REQUEST)
            else:
                if not check_password(data['password'],user.password):
                    result["Message"]="Invalid Credentials"
                    return Response(result,status=HTTP_401_UNAUTHORIZED)
                else:
                    student = Student.objects.filter(user=user).first()
                    token = RefreshToken.for_user(user)
                    data = {}
                    data['username'] = user.username
                    data['first_name'] = user.first_name
                    data['last_name'] = user.last_name
                    data['access'] = str(token.access_token)
                    data['token'] = str(token)
                    data['status'] = HTTP_200_OK
                    print(data)
                    return Response(data)
        except Exception as ex:
            print(str(ex))
            return Response("Success")
        

def sign_in(request):
    return render(request,'student_sign_in.html')