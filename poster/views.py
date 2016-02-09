from django.shortcuts import render_to_response

from poster.models import Category
from poster.models import Post

def one_post(request, idpost):
    post = Post.objects.get(id=idpost)
    
    return render_to_response(
        "post.html",
        {
            "post":post,
        },
    )

def home(request):
    posts = Post.objects.order_by("-creation_date")
    
    return render_to_response(
        "home.html",
        {
            "posts":posts,
        },
    )

def posts_by_category(request, idcategory):
    category = Category.objects.get(id=idcategory)
    posts = category.post_set.order_by("-creation_date")
    
    return render_to_response(
        "home.html",
        {
            "posts":posts,
        },
    )