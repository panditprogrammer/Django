from django.urls import path
from . import views

"""this is custom created file"""
# urls configuration  

urlpatterns = [
    path('hello/',views.say_hello)
]