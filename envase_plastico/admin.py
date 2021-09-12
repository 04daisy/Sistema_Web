from django.contrib import admin
from .models import Bodega,Categoria,Ciudad, Detalle_factura,Producto


# Register your models here.
admin.site.register(Bodega)
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Detalle_factura)
admin.site.register(Producto)

