from rest_framework import serializers
from .models import Clientes, Productos, Empresas, Proveedores, Empleados, Factura

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer(read_only=True)
    empleado = EmpleadosSerializer(read_only=True)
    producto = ProductosSerializer(read_only=True)
    
    class Meta:
        model = Factura
        fields = '__all__'
