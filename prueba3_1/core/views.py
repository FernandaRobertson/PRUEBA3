from django.shortcuts import render
from .models import Libro
from .form import LibroForm

# Create your views here.
def home(request):
    
    return render(request, 'core/home.html')

def libros(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/libros.html', datos)

def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_libros.html', datos)

def mod_libros(request, id):
    libros = Libro.objects.get(isbn=id)
    datos = {
        'mod': LibroForm(instance=libros)
    }
    return render(request, 'core/mod_libros.html', datos)