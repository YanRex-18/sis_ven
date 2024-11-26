from rest_framework import viewsets
from .serializer import ClientesSerializer,EmpleadosSerializer,EmpresasSerializer,ProductosSerializer,ProveedoresSerializer,FacturaSerializer
from .models import Clientes, Empleados, Empresas, Productos, Proveedores, Factura


# Create your views here.

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    #queryset = Factura.objects.filter(cliente=request.user)
    #serializer_class = FacturaSerializer(queryset, many=True)
