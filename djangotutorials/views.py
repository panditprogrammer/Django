from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world")

def indexHtml(request):
    return render(request,"index.html")

