from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# custom view function
# def say_hello(request):
#     return HttpResponse('hello World')

def say_hello(request):
    return render(request,'index.html',{'name':'Django'})