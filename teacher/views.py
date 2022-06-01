from django.shortcuts import render
from .models import Teacher

def root(request):
    data = Teacher.objects.filter().prefetch_related("Teacher_Educaional_Qualification","Teacher_Experience")
    return render(request,'teacher.html',{'value':data})

def index(request):
    data=Teacher.objects.filter().all()
    return render(request,'teacher_index.html',{'data':data})


def teacher_list(request):
    return render(request, 'teacher_list.html')


from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import TeacherListSerializer
from django.db.models import Q
class TeacherList(ListAPIView):
   permission_classes = []
   def get(self, request):
        # data_val = Teacher.objects.filter(salary__gte=50000).all()
        # data_val = Teacher.objects.filter(salary__lte=50000).all()
        # data_val = Teacher.objects.filter(salary__gt=50000).all()
        # data_val = Teacher.objects.filter(salary__lt=50000).all()
        # data_val = Teacher.objects.filter(Q(salary=50000) | Q(salary=5000) | Q(salary= 110000)).all()
        data_val = Teacher.objects.filter().all()
        # names = request.GET.get('first_name')
        # emails = request.GET.get('email')
        # if names:
        # #    data_val = Teacher.objects.filter(id=id).all()
        #     data_val = data_val.filter(first_name__icontains=names).all()
        # if emails:
        #     data_val = data_val.filter(email__icontains=emails).all()

        data_val = TeacherListSerializer(data_val, many=True).data
        return Response(data_val)



from rest_framework.utils import json
class NewTeacherAdd(CreateAPIView):
    permission_classes=[]
    def post(self,request,*args,**kwargs):
        try:
            data_value = json.loads(request.body)
            teacher = Teacher()
            if 'first_name' not in data_value or data_value['first_name'] == '':
                return Response("Please Fill your first name")
            teacher.first_name = data_value['first_name']
            teacher.last_name = data_value['last_name']
            teacher.father_name = data_value['father_name']
            teacher.mother_name = data_value['mother_name']
            teacher.gender = data_value['gender']
            teacher.religion = data_value['religion']
            teacher.email = data_value['email']
            teacher.fax = data_value['fax']
            teacher.blood_group = data_value['blood_group']
            teacher.phone = data_value['phone']
            teacher.birth_date = data_value['birth_date']
            teacher.joining_date = data_value['joining_date']
            teacher.retirement_date = data_value['retirement_date']
            teacher.address = data_value['address']
            teacher.save()
            return Response("Success")
        except Exception as ex:
            return Response({"Please fill the": str(ex)}, status=400)




class TeacherEdit(CreateAPIView):
    perimission_classes = []
    def post (self, request, *args, **kwargs):
        try:
            data_value = json.loads(request.body)
            teacher = Teacher.objects.filter(id=self.kwargs['id']).first()
            teacher.first_name = data_value['first_name']
            teacher.last_name = data_value['last_name']
            teacher.father_name = data_value['father_name']
            teacher.mother_name = data_value['mother_name']
            teacher.gender = data_value['gender']
            teacher.religion = data_value['religion']
            teacher.email = data_value['email']
            teacher.fax = data_value['fax']
            teacher.blood_group = data_value['blood_group']
            teacher.phone = data_value['phone']
            teacher.joining_date = data_value['joining_date']
            teacher.retirement_date = data_value['retirement_date']
            teacher.address = data_value['address']
            teacher.save()
            return Response("Success")
        except Exception as ex:
            return Response({"Error", str(ex)}, status=400)




def teacher_details(request, id):
    return render(request, 'teacher_details.html')

from .serializers import TeacherDetailsSerializer

class TeacherDetailsApi(ListAPIView):
    permission_classes = []
    def get(self, request, id):
        data_val = Teacher.objects.filter(id=id).first()
        data_val = TeacherDetailsSerializer(data_val).data
        return Response(data_val)