from django.urls import path
from .views import root,index,TeacherList,teacher_details,teacher_list,NewTeacherAdd,TeacherEdit,TeacherDetailsApi

urlpatterns = [
    # path('', root),
    path('', index),
    path('teacher_list/', teacher_list),
    path('teacher_details/<str:id>/', teacher_details),
    #api
    path('teacher_details_api/<str:id>/', TeacherDetailsApi.as_view()),
    path('teacher_list_api/', TeacherList.as_view()),
    path('teacher_create/', NewTeacherAdd.as_view()),
    path('teacher_edit/<str:id>/', TeacherEdit.as_view()),
]