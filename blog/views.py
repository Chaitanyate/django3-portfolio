from django.shortcuts import render,get_object_or_404
from .models import blog
def all_blog(request):
    blogs=blog.objects.all()
    return render(request,'blog/all_blog.html',{'blogs':blogs})

def details(request,blog_id):
    blogi=get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/details.html',{'id':blogi})