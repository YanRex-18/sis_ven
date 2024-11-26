from django.urls import path,include
from rest_framework import routers
from vent_app import views

router = routers.DefaultRouter()

router.register(r'clientes', views.ClientesViewSet)

router.register(r'empleados', views.EmpleadosViewSet)

router.register(r'productos', views.ProductosViewSet)

router.register(r'facturas', views.FacturaViewSet)

router.register(r'proveedores', views.ProveedoresViewSet)

router.register(r'empresas', views.EmpresasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

