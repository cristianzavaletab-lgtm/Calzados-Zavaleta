# calzados_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, CalzadoViewSet

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'calzados', CalzadoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]