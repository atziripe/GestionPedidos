from django.shortcuts import render
from blog.models import Post, Categorias

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/Blog.html", {"posts":posts})

def categoria(request, categoria_id):
    cat = Categorias.objects.get(id = categoria_id)
    postCat = Post.objects.filter(Categorias=cat)
    return render(request, "blog/Categorias.html",{"categoria": cat, "posts":postCat})
