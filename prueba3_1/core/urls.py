from django.urls import path
from .views import libros, mod_libros, form_libro, home

urlpatterns = [
    path('', home, name="home"),
    path('libros', libros, name="libros"),
    path('form_libros', form_libro, name="form_libros"),
    path('mod_libros/<id>', mod_libros, name="mod_libros"),
]