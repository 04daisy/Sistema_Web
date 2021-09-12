
"""Proyecto_3F_Sistema_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    Este archivo es de la aplicacion envase_plastico
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo),
    path('daisy/', views.miprimerfuncion),

    # OPERACIONES PARA CALCULADORA #
#    path('sumar/', views.sumar, name="sumar"),

# OPERACIONES PARA CALCULADORA #
#    path('restar/', views.restar, name="restar"),


##--------------------------------------------------------------------------------------------------------------

    # RUTAS PARA EL CRUD DE LA ENTIDAD BODEGA#
    path('consultar_bodega/', views.consultar_bodega, name="consultar_bodega"),
    path('crear_bodega/', views.crear_bodega, name="crear_bodega"),
    path('modificar_bodega/<int:id>', views.modificar_bodega, name="modificar_bodega"),
    path('eliminar_bodega/<int:id>', views.eliminar_bodega, name="eliminar_bodega"),


    # RUTAS PARA EL CRUD DE LA ENTIDAD CATEGORIA#
    path('consultar_categoria/', views.consultar_categoria, name="consultar_categoria"),
    path('crear_categoria/', views.crear_categoria, name="crear_categoria"),
    path('modificar_categoria/<int:id>', views.modificar_categoria, name="modificar_categoria"),
    path('eliminar_categoria/<int:id>', views.eliminar_categoria, name="eliminar_categoria"),


    # RUTAS PARA EL CRUD DE LA ENTIDAD CIUDAD#
    path('consultar_cuidad/', views.consultar_ciudad, name="consultar_ciudad"),
    path('crear_ciudad/', views.crear_ciudad, name="crear_ciudad"),
    path('modificar_ciudad/<int:id>', views.modificar_ciudad, name="modificar_ciudad"),
    path('eliminar_ciudad/<int:id>', views.eliminar_ciudad, name="eliminar_ciudad"),


    # RUTAS PARA EL CRUD DE LA ENTIDAD DETALLE_FACTURA#
    path('consultar_detalle_factura/', views.consultar_detalle_factura, name="consultar_detalle_factura"),
    path('crear_detalle_factura/', views.crear_detalle_factura, name="crear_detalle_factura"),
    path('modificar_detalle_factura/<int:id>', views.modificar_detalle_factura, name="modificar_detalle_factura"),
    path('eliminar_detalle_factura/<int:id>', views.eliminar_detalle_factura, name="eliminar_detalle_factura"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD ESTADO_FACTURAS#
    path('consultar_estado_facturas/', views.consultar_estado_facturas, name="consultar_estado_facturas"),
    path('crear_estado_facturas/', views.crear_estado_facturas, name="crear_estado_facturas"),
    path('modificar_estado_facturas/<int:id>', views.modificar_estado_facturas, name="modificar_estado_facturas"),
    path('eliminar_estado_facturas/<int:id>', views.eliminar_estado_facturas, name="eliminar_estado_facturas"),


    # RUTAS PARA EL CRUD DE LA ENTIDAD FACTURA#
    path('consultar_factura/', views.consultar_factura, name="consultar_factura"),
    path('crear_factura/', views.crear_factura, name="crear_factura"),
    path('modificar_factura/<int:id>', views.modificar_factura, name="modificar_factura"),
    path('eliminar_factura/<int:id>', views.eliminar_factura, name="eliminar_factura"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD FORMA_PAGO#
    path('consultar_forma_pago/', views.consultar_forma_pago, name="consultar_forma_pago"),
    path('crear_forma_pago/', views.crear_forma_pago, name="crear_forma_pago"),
    path('eliminar_forma_pago/', views.eliminar_forma_pago, name="eliminar_forma_pago"),
    path('modificar_forma_pago/', views.modificar_forma_pago, name="modificar_forma_pago"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD INVENTARIO#
    path('consultar_inventario/', views.consultar_inventario, name="consultar_inventario"),
    path('crear_inventario/', views.crear_inventario, name="crear_inventario"),
    path('eliminar_inventario/', views.eliminar_inventario, name="eliminar_inventario"),
    path('modificar_inventario/', views.modificar_inventario, name="modificar_inventario"),


    # RUTAS PARA EL CRUD DE LA ENTIDAD OPCIONES#
    path('consultar_opciones/', views.consultar_opciones, name="consultar_opciones"),
    path('crear_opciones/', views.crear_opciones, name="crear_opciones"),
    path('eliminar_opciones/', views.eliminar_opciones, name="eliminar_opciones"),
    path('modificar_opciones/', views.modificar_opciones, name="modificar_opciones"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD PRODUCTO#
    path('consultar_producto/', views.consultar_producto, name="consultar_producto"),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('eliminar_producto/', views.eliminar_producto, name="eliminar_producto"),
    path('modificar_producto/', views.modificar_producto, name="modificar_producto"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD PROVEEDOR#
    path('consultar_proveedor/', views.consultar_proveedor, name="consultar_proveedor"),
    path('crear_proveedor/', views.crear_proveedor, name="crear_proveedor"),
    path('eliminar_proveedor/', views.eliminar_proveedor, name="eliminar_proveedor"),
    path('modificar_proveedor/', views.modificar_proveedor, name="modificar_proveedor"),


    # RUTAS PARA EL CRUD DE LA ENTIDAD ROLES#
    path('consultar_roles/', views.consultar_roles, name="consultar_roles"),
    path('crear_roles/', views.crear_roles, name="crear_roles"),
    path('eliminar_roles/', views.eliminar_roles, name="eliminar_roles"),
    path('modificar_roles/', views.modificar_roles, name="modificar_roles"),

   # RUTAS PARA EL CRUD DE LA ENTIDAD USUARIO_FACTURAS#
    path('consultar_usuario_facturas/', views.consultar_usuario_facturas, name="consultar_usuario_facturas"),
    path('crear_usuario_facturas/', views.crear_usuario_facturas, name="crear_usuario_facturas"),
    path('eliminar_usuario_facturas/', views.eliminar_usuario_facturas, name="eliminar_usuario_facturas"),
    path('modificar_usuario_facturas/', views.modificar_usuario_facturas, name="modificar_usuario_facturas"),


   # RUTAS PARA EL CRUD DE LA ENTIDAD USUARIO_ROLES#
    path('consultar_usuario_roles/', views.consultar_usuario_roles, name="consultar_usuario_roles"),
    path('crear_usuario_roles/', views.crear_usuario_roles, name="crear_usuario_roles"),
    path('eliminar_usuario_roles/', views.eliminar_usuario_roles, name="eliminar_usuario_roles"),
    path('modificar_usuario_roles/', views.modificar_usuario_roles, name="modificar_usuario_roles"),


    #RUTAS PARA EL CRUD DE LA ENTIDAD USUARIOS#
    path('consultar_usuarios/', views.consultar_usuarios, name="consultar_usuarios"),
    path('crear_usuarios/', views.crear_usuarios, name="crear_usuarios"),
    path('eliminar_usuarios/', views.eliminar_usuarios, name="eliminar_usuarios"),
    path('modificar_usuarios/', views.modificar_usuarios, name="modificar_usuarios"),


]
