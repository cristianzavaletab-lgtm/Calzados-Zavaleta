# calzados_api/models.py
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Calzado(models.Model):
    modelo = models.CharField(max_length=100)
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='calzados/', null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='calzados')
    
    def __str__(self):
        return self.modelo