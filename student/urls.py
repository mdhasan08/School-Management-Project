from django.urls import path
from .views import root,root1,header,student_index,student_list,student_details,StudentListApi,sign_up,sign_in,SignUpApi,OtpCheckApi,StudentSignInApi, log_out, StudentDetailsApi

urlpatterns = [
    path('root/', root),
    # path('class/<str:sc>/', root1),
    # path('header/', header),
    path('', student_index),
    path('student_sign_up/', sign_up),
    path('student_sign_in/', sign_in),
    path('student_list/', student_list),
    path('student_details/<str:id>/', student_details),
    path('log_out/', log_out),
    #api
    path('student_list_api/', StudentListApi.as_view()),
    path('student_sign_up_api/', SignUpApi.as_view()),
    path('student_otp_check_api/', OtpCheckApi.as_view()),
    path('student_sign_in_api/', StudentSignInApi.as_view()),
    path('student_details_api/<str:id>/', StudentDetailsApi.as_view()),
]
