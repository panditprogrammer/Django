from django.http import HttpResponse
from django.shortcuts import render


# render html file 
def index(request):
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


def blogs(request):
    return render(request,"blogs.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")