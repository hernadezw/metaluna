from django.contrib import admin
from cliente.models import Cliente, TipoCliente, Municipio, Departamento, Direccion
# Register your models here.

admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Municipio)
admin.site.register(Departamento)
admin.site.register(Direccion)