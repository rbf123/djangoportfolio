from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
#def all_blogs(request):
#    blogs = Blog.objects.order_by('-date')[:10]
#   return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def all_blogs(request):
    blogs_list = Blog.objects.order_by('-date')
    paginator = Paginator(blogs_list, 10) # Show 10 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/all_blogs.html', {'page_obj': page_obj})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
    