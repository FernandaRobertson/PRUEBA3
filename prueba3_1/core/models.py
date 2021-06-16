from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

#modelo para libro

class Libro(models.Model):
    isbn= models.IntegerField( primary_key=True, verbose_name='ISBN')
    nombre= models.CharField(max_length=30, verbose_name='Nombre Libro')
    autor= models.CharField(max_length=40, verbose_name='Autor')
    descripcion= models.CharField(max_length=350, verbose_name='Descripcion')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __int__(self):
        return self.isbn

