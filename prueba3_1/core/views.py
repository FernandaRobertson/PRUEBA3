from django.shortcuts import render, redirect
from .models import Libro
from .form import LibroForm


# Create your views here.
def home(request):
    libros= Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/home.html', datos)

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
        formulario = LibroForm(request.POST, instance=libros)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'

    return render(request, 'core/form_libros.html', datos)

def eliminar_l(request, id):
    libro= Libro.objects.get(isbn=id)
    libro.delete()
    return redirect(to="libro")

def registro_us(request):
    return render(request, 'core/registro_us.html')

def crea_libro(request):
    datos = {
        'form': LibroForm()   
    }
    if request.method =='POST':
        formulario=LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"] = "Creado correctamente" 
    return render(request, 'core/crea_libro.html', datos)