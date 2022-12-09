from django.urls import path,include
from blog.views import *

urlpatterns = [
    path('',home,name='index'),
    path('<slug:slug>',detail_post,name='detail_post'),
    path('generales/',generales,name='generales'),
    path('videojuegos/',videojuegos,name = 'videojuegos'),
    path('programacion/',programacion,name = 'programacion'),
    path('tecnologia/',tecnologia,name = 'tecnologia'),
    path('tutoriales/',tutoriales,name = 'tutoriales'),
]
