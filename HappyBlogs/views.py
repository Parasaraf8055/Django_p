from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs

# Create your views here.

def All_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'All_blogs.html',{'blogs':blogs})

def create_blog(request):
    if request.method == 'POST':
        date=request.POST['date']
        time=request.POST['time']
        content=request.POST['content']
        name=request.POST['name']
        Blogs.objects.create(date=date,time=time,content=content,name=name)
        return redirect('All_blogs')
    
    return render(request, 'update_blogs.html')


def update_blog(request,id):
    blog=get_object_or_404(Blogs,pk=id)
    if request.method == 'POST':
        blog.date=request.POST['date']
        blog.time=request.POST['time']
        blog.content=request.POST['content']
        blog.name=request.POST['name']
        blog.save()
        return redirect('All_blogs')
    
    return render(request,'update_blogs.html',{'blog':blog})


def delete_blog(request,id):
    book = get_object_or_404(Blogs,pk=id)
    book.delete()
    return redirect('All_blogs')