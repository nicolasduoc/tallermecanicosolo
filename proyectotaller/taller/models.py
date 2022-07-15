from ast import Delete
from django.db import models

# Create your models here.
class Atencion(models.Model):
    id = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=200,verbose_name='descripcion')
    Imagen = models.ImageField(upload_to='imagenes/', null=True,verbose_name='imagen')
    Patente = models.CharField(max_length=6,verbose_name='patente')



    def __str__(self):
        fila = "Descripcion: " + self.Descripcion + " - " + "Patente: " + self.Patente
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.IntegerField()
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    rut= models.CharField(max_length=20,verbose_name='rut')
    correo = models.CharField(max_length=50,verbose_name='correo')
    
    def __str__(self):
        return self.nombre



