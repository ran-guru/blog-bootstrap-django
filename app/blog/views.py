from django.shortcuts import render
from blog.models import Post, Category




# Create your views here.
def home(request):

    posts = Post.objects.filter(
        state = True,
    )

    return render(request, 'index.html',{'posts': posts})

def detail_post(request,slug):

    post = Post.objects.get(slug = slug)
    print(slug)
    return render(request, 'post.html',{'post':post})

def generales(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Generales')
    )
    return render(request, 'generales.html',{'posts': posts})


def videojuegos(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Videojuegos')
    )
    return render(request,'videojuegos.html',{'posts': posts})

def programacion(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Programacion')
    )
    return render(request,'programacion.html',{'posts': posts})

def tecnologia(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Tecnologia')
    )
    return render(request,'tecnologia.html',{'posts': posts})

def tutoriales(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Tutoriales')
    )
    return render(request,'tutoriales.html',{'posts':posts})
