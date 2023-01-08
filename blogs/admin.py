from django.contrib import admin
from blogs.models import Blogs,Contact


# Register your models here to show in the admin panel
class BlogsPanel(admin.ModelAdmin):
    list_display = ('slug','title','description','img','category','added_on','updated_on')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')

admin.site.register(Blogs,BlogsPanel)
admin.site.register(Contact,ContactAdmin)
