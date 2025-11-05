# calzados_api/admin.py
from django.contrib import admin
from .models import Marca, Calzado

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'pais_origen']

@admin.register(Calzado)
class CalzadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'modelo', 'talla', 'color', 'precio', 'marca']