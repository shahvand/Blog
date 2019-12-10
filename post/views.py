from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponsePermanentRedirect
from .models import post
from .forms import PostForm
from django.contrib import messages
# Create your views here.


def index_view(request):
    posts = post.objects.all()
    return render(request,'post/index.html',{"posts":posts})

def create_view(request):
    
    form = PostForm(request.POST or None)
    if request.method == "POST":
        
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Post Created Successfuly")
            return HttpResponsePermanentRedirect(post.get_absolute_url())
        else:
            form = PostForm()
        
            
    
    context = {
        'form': form
    }
    return render(request,"post/form.html",context)

def detail_view(request, id):
    posts = get_object_or_404(post, id=id)
    return render(request,'post/detail.html',{"post": posts})

def update_view(request, id):
    posts = get_object_or_404(post, id=id)
    form = PostForm(request.POST or None, instance=posts)
    if form.is_valid():
        
        form.save()
        messages.success(request, "Post Edit Successfuly")
        return HttpResponsePermanentRedirect(posts.get_absolute_url())   
    context = {
        'form': form
    }
    return render(request,'post/form.html',context)

