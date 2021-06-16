from django.urls import path
from .views import libros, form_libro, home

urlpatterns = [
    path('', home, name="home"),
    path('libros', libros, name="libros"),
    path('form_libros/<id>', form_libro, name="form_libros"),
    
]