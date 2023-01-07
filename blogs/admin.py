from django.contrib import admin
from blogs.models import Blogs


# Register your models here to show in the admin panel
class BlogsPanel(admin.ModelAdmin):
    list_display = ('slug','title','description','img','category','added_on','updated_on')


admin.site.register(Blogs,BlogsPanel)
