from django.shortcuts import render ,get_object_or_404
from .models import Blog , CategoryBlog
# Create your views here.
def blog_list(request, category_slug=None):
    category = None
    categories = CategoryBlog.objects.all()
    blogs = Blog.objects.filter()
    if category_slug:
        category = get_object_or_404(CategoryBlog, slug=category_slug)
        blogs = Blog.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'blogs':blogs
    }
    return render(request, 'blog.html', context)

def blog_detail(request , id , slug):
    category = None
    categories = CategoryBlog.objects.all()
    blog = get_object_or_404(Blog  , id=id , slug=slug)
    blogs = Blog.objects.all()
    context = {
        'blog':blog,
        'blogs':blogs,
        'categories':categories


    }
    return render(request , 'single-blog.html' , context)

