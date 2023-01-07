from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world")

# render html file 
def indexHtml(request):
    # pass dynamic data  to html template 
    data = {   
        "title":"This is home  page title.",
        "pageContent":"This is page content.",
        "Students":[
            {"name":"Radhika","email":"radhika@gmail.com"},
            {"name":"Pradeep","email":"pradeep@gmail.com"},
            {"name":"Prity","email":"Prity@gmail.com"},
        ]
    }
    return render(request,"index.html",data)

