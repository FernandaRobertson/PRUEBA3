from django.urls import path
from .views import libros, form_libro, home, eliminar_l, registro_us, crea_libro

urlpatterns = [
    path('', home, name="home"),
    path('libros', libros, name="libro"),
    path('form_libros/<id>', form_libro, name="form_libros"),
    path('eliminarlibro/<id>', eliminar_l, name="eliminar_l"),
    path('usuario', registro_us, name="registro_us"),
    path('crea_libro', crea_libro, name="crea_libro"),
]