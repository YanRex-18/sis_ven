from django.contrib import admin
from .models import Clientes,Productos,Proveedores,Empleados,Empresas,Factura

# Register your models here.
admin.site.register(Clientes)

admin.site.register(Productos)

admin.site.register(Proveedores)

admin.site.register(Empleados)

admin.site.register(Empresas)

admin.site.register(Factura)
