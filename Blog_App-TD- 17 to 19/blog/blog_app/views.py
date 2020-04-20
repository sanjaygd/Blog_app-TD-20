from django.shortcuts import render,get_object_or_404

from .models import Post
from .forms import PostForm

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request,'blog_app/post_list.html',context)


def post_details(request,pk=None):
    instance = get_object_or_404(Post,pk=pk)
    context = {
        'obj_details':instance
    }
    return render(request,'blog_app/post_details.html',context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    # if request.method == 'POST':
    #     print(request.POST)
    context = {
        'form':form
    }
    return render(request, 'blog_app/post_create.html',context)

