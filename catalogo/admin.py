from django.contrib import admin

# Register your models here.

from .models import Proveedor, Categoria, Producto, DetalleProducto

admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleProducto)
