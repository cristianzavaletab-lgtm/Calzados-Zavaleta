# calzados_api/views.py
from rest_framework import viewsets
from .models import Marca, Calzado
from .serializers import MarcaSerializer, CalzadoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CalzadoViewSet(viewsets.ModelViewSet):
    queryset = Calzado.objects.all()
    serializer_class = CalzadoSerializer