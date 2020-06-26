from django.contrib import admin
from blog.models import Blog 
# Register your models here.

#admin.site.register(Blog)

class blogAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":("css/main.css",)
        }
        js=("js/blog.js",)

admin.site.register(Blog,blogAdmin)