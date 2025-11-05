# calzados_api/serializers.py
from rest_framework import serializers
from .models import Marca, Calzado

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CalzadoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source='marca.nombre', read_only=True)
    
    class Meta:
        model = Calzado
        fields = '__all__'