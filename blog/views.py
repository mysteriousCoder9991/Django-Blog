from django.shortcuts import render,HttpResponse
from blog.models import Blog
import math
# Create your views here.
def home(request):
    #return HttpResponse("This is home")
    return render(request,'index.html')

def blog(request):
     no_of_post=4
     page=request.GET.get('page')
     if page is None:
          page=1
     else:
          page=int(page)
     print("pages is {}".format(page))
     blogs=Blog.objects.all()
     length=len(blogs)
     blogs=blogs[(page-1)*no_of_post:page*no_of_post]
     if page>1:
          prev=page-1
     else:
          prev=None
     #print("blog lenght= {}".format(len(blogs)))
     if page < math.ceil(length/no_of_post):
          nxt=page+1
     else:
          nxt=None
     print(prev,nxt)
     context={'blogs':blogs,'prev':prev,'nxt':nxt}
     return render(request,'bloghome.html',context)

def blogPost(request,slug):
     blog=Blog.objects.filter(slug=slug).first()
     context={'blog':blog}
     return render(request,'blogpost.html',context)


def contact(request):
     return render(request,'contact.html')
def search(request):
     return render(request,'search.html')

def error(request,slug):
     context={'slug':slug}
     return render(request,'error.html',context)

def endList(request):
     return render(request,'endList.html')