from django.shortcuts import render
from .models import Libro
from .form import LibroForm


# Create your views here.
def home(request):
    libros= Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/home.html',datos)

def libros(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/libros.html', datos)

def form_libro(request, id):
    libros = Libro.objects.get(isbn=id)
    datos = {
        'form': LibroForm(instance=libros)
    }
    if request.method=='POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'

    return render(request, 'core/form_libros.html', datos)

