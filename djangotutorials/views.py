from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Blogs


# render html file 
def index(request):
    # pass dynamic data  to html template 
    data = {   
        "title":"This is home  page title.",
        "Students":[
            {"name":"Radhika","email":"radhika@gmail.com"},
            {"name":"Pradeep","email":"pradeep@gmail.com"},
            {"name":"Prity","email":"Prity@gmail.com"},
        ]
    }
    return render(request,"index.html",data)




def blogs(request):
    allBlogs = searchBlogs = Blogs.objects.all().order_by("-updated_on")
    search = "" 
    if 'search' in request.GET:
        search = request.GET['search'].strip()
        searchBlogs = Blogs.objects.filter(title__contains=search)
    return render(request,"blogs.html",{"allBlogs":allBlogs,"searchBlogs":searchBlogs,"search":search})
    



def blogsDetails(request,slug):
    allBlogs = Blogs.objects.all().order_by("-updated_on")
    try:
        blog = Blogs.objects.get(slug=slug)
    except Exception as e:
        print(e)
        return redirect('/blogs',{"allBlogs":allBlogs})
    return render(request,"single.html",{"allBlogs":allBlogs,"blog":blog})



def about(request):
    return render(request,"about.html")



def contact(request):
    return render(request,"contact.html")