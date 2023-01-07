from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world")

# render html file 
def indexHtml(request):
    data = {
        "title":"This is home  page title.",
        "pageContent":"This is page content."
    }
    return render(request,"index.html",data)

