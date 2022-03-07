from django.http import HttpResponse
from django.shortcuts import render


# def root(request):
#     text = "Welcome to school"
#     return HttpResponse(text)

def root(request):
    return render(request,'root.html')