from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import BodegaForm
from .forms import CategoriaForm
from .forms import CiudadForm
from .forms import Detalle_facturaForm
from .forms import Estado_facturasForm
from .forms import FacturaForm
from .forms import Forma_pagoForm
from .forms import InventarioForm
from .forms import OpcionesForm
from .forms import ProductoForm
from .forms import ProveedorForm
from .forms import RolesForm
from .forms import Usuario_facturasForm
from .forms import Usuario_rolesForm
from .forms import UsuariosForm
from .models import Bodega
from .models import Categoria
from .models import Ciudad
from .models import Detalle_factura
from .models import Estado_facturas
from .models import Factura
from .models import Forma_pago
from .models import Inventario
from .models import Opciones
from .models import Producto
from .models import Proveedor
from .models import Roles
from .models import Usuario_facturas
from .models import Usuario_roles
from .models import Usuarios





# Create your views here.
def saludo(request):
    return HttpResponse("Hola Mundo!!")


def miprimerfuncion(request):
    return render(request, "base1.html")


### FUNCIONES PARA CALCULADORA ###
# def sumar(request):
#   if request.method == "POST":
#        valoresform = ValoresForm(request.POST)
#       if (valoresform.is_valid()):
#           valor1 = valoresform.cleaned_data['valor1']
#           valor2 = valoresform.cleaned_data['valor2']
#          total = valor1 + valor2
# return redirect("sumar")

#  else:
#      valoresform = ValoresForm()
#      total = 0
#  return render(request, "sumar.html", {'formulario':valoresform, 'suma':total})


### FUNCIONES PARA CALCULADORA ###
# def restar(request):
#    if request.method == "POST":
#        valoresform = ValoresForm(request.POST)
#        if (valoresform.is_valid()):
#            valor1 = valoresform.cleaned_data['valor1']
#            valor2 = valoresform.cleaned_data['valor2']
#            total = valor1 - valor2
# return redirect("restar")

#    else:
#        valoresform = ValoresForm()
#        total = 0
#    return render(request, "restar.html", {'formulario':valoresform, 'resta':total})


### --------------------------------------------------------------------------------------------------------------------

### CRUD PARA LA ENTIDAD BODEGA
def consultar_bodega(request):
    bodegas = Bodega.objects.all()
    return render(request, "bodega/consultar_bodega.html", {'bodegas_ls': bodegas})


def crear_bodega(request):
    if request.method == "POST":
        bodegaForm = BodegaForm(request.POST)
        if bodegaForm.is_valid():
            bodegaForm.save()
            return redirect('consultar_bodega')
        else:
            bodegaForm = BodegaForm()

    else:
        bodegaForm = BodegaForm()
    return render(request, "bodega/crear_bodega.html", {'bodegaForm': bodegaForm})


def modificar_bodega(request, id):
    if request.method == "POST":
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega)
        if bodegaForm.is_valid():
            bodegaForm.save()
            return redirect('consultar_bodega')
        else:
            bodegaForm = BodegaForm(instance=bodega)

    else:  ##GET
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(instance=bodega)
    return render(request, "bodega/modificar_bodega.html", {'bodegaForm': bodegaForm})


def eliminar_bodega(request, id):
    if request.method == "POST":
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega)
        if bodegaForm.is_valid():
            bodega.estado = 0
            bodega.save()
            # bodegaForm.
            return redirect('consultar_bodega')
    else:  ## GET
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(instance=bodega)
    return render(request, "bodega/eliminar_bodega.html", {'bodegaForm': bodegaForm})


###CRUD PARA LA ENTIDAD CATEGORIA
def consultar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, "categoria/consultar_categoria.html", {'categorias_ls': categorias})


def crear_categoria(request):
    if request.method == "POST":
        categoriaForm = CategoriaForm(request.POST)
        if categoriaForm.is_valid():
            categoriaForm.save()
            return redirect('consultar_categoria')
        else:
            categoriaForm = CategoriaForm()

    else:
        categoriaForm = CategoriaForm()
    return render(request, "categoria/crear_categoria.html", {'categoriaForm': categoriaForm})


def modificar_categoria(request, id):
    if request.method == "POST":
        categoria = get_object_or_404(Categoria, pk=id)
        categoriaForm = CategoriaForm(request.POST or None, instance=categoria)
        if categoriaForm.is_valid():
            categoriaForm.save()
            return redirect('consultar_categoria')
        else:
            categoriaForm = CategoriaForm(instance=categoria)

    else:  ##GET
        categoria = get_object_or_404(Categoria, pk=id)
        categoriaForm = CategoriaForm(instance=categoria)
    return render(request, "categoria/modificar_categoria.html", {'categoriaForm': categoriaForm})


def eliminar_categoria(request, id):
    if request.method == "POST":
        categoria = get_object_or_404(Bodega, pk=id)
        categoriaForm = CategoriaForm(request.POST or None, instance=categoria)
        if categoriaForm.is_valid():
            categoria.estado = 0
            categoria.save()
            # categoriaForm.
            return redirect('consultar_categoria')
    else:  ## GET
        categoria = get_object_or_404(Categoria, pk=id)
        categoriaForm = CategoriaForm(instance=categoria)
    return render(request, "categoria/eliminar_categoria.html", {'categoriaForm': categoriaForm})


### CRUD PARA LA ENTIDAD CIUDAD
def consultar_ciudad(request):
    ciudades = Ciudad.objects.all()
    return render(request, "ciudad/consultar_ciudad.html", {'ciudades_ls': ciudades})


def crear_ciudad(request):
    if request.method == "POST":
        ciudadForm = CiudadForm(request.POST)
        if ciudadForm.is_valid():
            ciudadForm.save()
            return redirect('consultar_ciudad')
        else:
            ciudadForm = CiudadForm()

    else:
        ciudadForm = CiudadForm()
    return render(request, "ciudad/crear_ciudad.html", {'ciudadForm': ciudadForm})


def modificar_ciudad(request, id):
    if request.method == "POST":
        ciudad = get_object_or_404(Ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudad)
        if ciudadForm.is_valid():
            ciudadForm.save()
            return redirect('consultar_ciudad')
        else:
            ciudadForm = CiudadForm(instance=ciudad)

    else:  ##GET
        ciudad = get_object_or_404(Ciudad, pk=id)
        ciudadForm = CiudadForm(instance=ciudad)
    return render(request, "ciudad/modificar_ciudad.html", {'ciudadForm': ciudadForm})


def eliminar_ciudad(request, id):
    if request.method == "POST":
        ciudad = get_object_or_404(Ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudad)
        if ciudadForm.is_valid():
            ciudad.estado = 0
            ciudad.save()
            # ciudadForm.
            return redirect('consultar_ciudad')
    else:  ## GET
        ciudad = get_object_or_404(Ciudad, pk=id)
        ciudadForm = CiudadForm(instance=ciudad)
    return render(request, "ciudad/eliminar_ciudad.html", {'ciudadForm': ciudadForm})


### CRUD PARA LA ENTIDAD DETALLE_FACTURA
def consultar_detalle_factura(request):
    detalles_facturas = Detalle_factura.objects.all()
    return render(request, "detalle_factura/consultar_detalle_factura.html", {'detalles_facturas_ls': detalles_facturas})


def crear_detalle_factura(request):
    if request.method == "POST":
        detalle_facturaForm = Detalle_facturaForm(request.POST)
        if detalle_facturaForm.is_valid():
            detalle_facturaForm.save()
            return redirect('consultar_detalle_factura')
        else:
            detalle_facturaForm = Detalle_facturaForm()

    else:
        detalle_facturaForm = Detalle_facturaForm()
    return render(request, "detalle_factura/crear_detalle_factura.html", {'detalle_facturaForm': detalle_facturaForm})


def modificar_detalle_factura(request, id):
    if request.method == "POST":
        detalle_factura = get_object_or_404(Detalle_factura, pk=id)
        detalle_facturaForm = BodegaForm(request.POST or None, instance=detalle_factura)
        if detalle_facturaForm.is_valid():
            detalle_facturaForm.save()
            return redirect('consultar_detalle_factura')
        else:
            detalle_facturaForm = Detalle_facturaForm(instance=detalle_factura)

    else:  ##GET
        detalle_factura = get_object_or_404(Detalle_factura, pk=id)
        detalle_facturaForm = Detalle_facturaForm(instance=detalle_factura)
    return render(request, "detalle_factura/modificar_detalle_factura.html", {'detalle_facturaForm': detalle_facturaForm})


def eliminar_detalle_factura(request, id):
    if request.method == "POST":
        detalle_factura = get_object_or_404(Detalle_factura, pk=id)
        detalle_facturaForm = Detalle_facturaForm(request.POST or None, instance=detalle_factura)
        if detalle_facturaForm.is_valid():
            detalle_factura.estado = 0
            detalle_factura.save()
            # detalle_facturaForm.
            return redirect('consultar_detalle_factura')
    else:  ## GET
        detalle_factura = get_object_or_404(Detalle_factura, pk=id)
        detalle_facturaForm = Detalle_factura(instance=detalle_factura)
    return render(request, "detalle_factura/eliminar_detalle_factura.html", {'detalle_facturaForm': detalle_facturaForm})




### CRUD PARA LA ENTIDAD ESTADO_FACTURAS
def consultar_estado_facturas(request):
    estados_facturas = Estado_facturas.objects.all()
    return render(request, "estado_facturas/consultar_estado_facturas.html", {'estados_facturas_ls': estados_facturas})


def crear_estado_facturas(request):
    if request.method == "POST":
        estado_facturasForm = Estado_facturasForm(request.POST)
        if estado_facturasForm.is_valid():
            estado_facturasForm.save()
            return redirect('consultar_estado_facturas')
        else:
            estado_facturasForm = Estado_facturasForm()

    else:
        estado_facturasForm = Estado_facturasForm()
    return render(request, "estado_facturas/crear_estado_facturas.html", {'estado_facturasForm': estado_facturasForm})


def modificar_estado_facturas(request, id):
    if request.method == "POST":
        estado_facturas = get_object_or_404(Estado_facturas, pk=id)
        estado_facturasForm = Estado_facturasForm(request.POST or None, instance=estado_facturas)
        if estado_facturasForm.is_valid():
            estado_facturasForm.save()
            return redirect('consultar_estado_facturas')
        else:
            estado_facturasForm = Estado_facturasForm(instance=estado_facturas)

    else:  ##GET
        estado_facturas = get_object_or_404(Estado_facturas, pk=id)
        estado_facturasForm = Estado_facturasForm(instance=estado_facturas)
    return render(request, "estado_facturas/modificar_estado_facturas.html", {'estado_facturasForm': estado_facturasForm})


def eliminar_estado_facturas(request, id):
    if request.method == "POST":
        estado_facturas = get_object_or_404(Estado_facturas, pk=id)
        estado_facturasForm = Estado_facturasForm(request.POST or None, instance=estado_facturas)
        if estado_facturasForm.is_valid():
            estado_facturasForm.estado = 0
            estado_facturas.save()
            # estado_facturasForm.
            return redirect('consultar_estado_facturas')
    else:  ## GET
        estado_facturas = get_object_or_404(Estado_facturas, pk=id)
        estado_facturasForm = Estado_facturasForm(instance=estado_facturas)
    return render(request, "estado_facturas/eliminar_estado_facturas.html", {'estado_facturasForm': estado_facturasForm})



### CRUD PARA LA ENTIDAD FACTURA
def consultar_factura(request):
    facturas = Factura.objects.all()
    return render(request, "factura/consultar_factura.html", {'facturas_ls': facturas})


def crear_factura(request):
    if request.method == "POST":
        facturaForm = FacturaForm(request.POST)
        if facturaForm.is_valid():
            facturaForm.save()
            return redirect('consultar_factura')
        else:
            facturaForm = FacturaForm()

    else:
        facturaForm = FacturaForm()
    return render(request, "factura/crear_factura.html", {'facturaFrom': facturaForm})


def modificar_factura(request, id):
    if request.method == "POST":
        factura = get_object_or_404(Factura, pk=id)
        factura_Form = FacturaForm(request.POST or None, instance=factura)
        if factura_Form.is_valid():
            factura_Form.save()
            return redirect('consultar_factura')
        else:
            factura_Form = FacturaForm(instance=factura)

    else:  ##GET
        factura = get_object_or_404(Factura, pk=id)
        factura_Form = FacturaForm(instance=factura)
    return render(request, "factura/modificar_factura.html", {'facturaForm': factura_Form})


def eliminar_factura(request, id):
    if request.method == "POST":
        factura = get_object_or_404(Factura, pk=id)
        facturaForm = FacturaForm(request.POST or None, instance=factura)
        if facturaForm.is_valid():
            factura.estado = 0
            factura.save()
            # facturaForm.
            return redirect('consultar_factura')
    else:  ## GET
        factura = get_object_or_404(Factura, pk=id)
        facturaForm = FacturaForm(instance=factura)
    return render(request, "factura/eliminar_factura.html", {'facturaFrom': facturaForm})


### CRUD PARA LA ENTIDAD FORMA_PAGO
def consultar_forma_pago(request):
    forma_pagos = Forma_pago.objects.all()
    return render(request, "forma_pago/consultar_forma_pago.html", {'forma_pagos_ls': forma_pagos})


def crear_forma_pago(request):
    if request.method == "POST":
        forma_pagoForm = Forma_pagoForm(request.POST)
        if forma_pagoForm.is_valid():
            forma_pagoForm.save()
            return redirect('consultar_forma_pago')
        else:
            forma_pagoForm = Forma_pagoForm()

    else:
        forma_pagoForm = Forma_pagoForm()
    return render(request, "forma_pago/crear_forma_pago.html", {'forma_pagoForm': forma_pagoForm})


def modificar_forma_pago(request, id):
    if request.method == "POST":
        forma_pago = get_object_or_404(Forma_pago, pk=id)
        forma_pagoForm = Forma_pagoForm(request.POST or None, instance=forma_pago)
        if forma_pagoForm.is_valid():
            forma_pagoForm.save()
            return redirect('consultar_forma_pago')
        else:
            forma_pagoForm = Forma_pagoForm(instance=forma_pago)

    else:  ##GET
        forma_pago = get_object_or_404(Forma_pago, pk=id)
        forma_pagoForm = Forma_pagoForm(instance=forma_pago)
    return render(request, "forma_pago/modificar_forma_pago.html", {'forma_pagoForm': forma_pagoForm})


def eliminar_forma_pago(request, id):
    if request.method == "POST":
        forma_pago = get_object_or_404(Forma_pago, pk=id)
        forma_pagoForm = Forma_pagoForm(request.POST or None, instance=forma_pago)
        if forma_pagoForm.is_valid():
            forma_pago.estado = 0
            bodega.save()
            # bodegaForm.
            return redirect('consultar_bodega')
    else:  ## GET
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(instance=bodega)
    return render(request, "bodega/eliminar_bodega.html", {'bodegaForm': bodegaForm})


### CRUD PARA LA ENTIDAD INVENTARIO
def consultar_inventario(request):
    if request.method == "POST":
       inventarioForm = InventarioForm(request.POST)
       if inventarioForm.is_valid():
           inventarioForm.save()
           return redirect('consultar_inventario')
       else:
           inventarioForm = InventarioForm()

    else:
        inventarioForm = InventarioForm()
    return render(request, "inventario/consultar_inventario.html", {'inventarioForm': inventarioForm})


def crear_inventario(request):
    if request.method == "POST":
       inventarioForm = InventarioForm(request.POST)
       if inventarioForm.is_valid():
           inventarioForm.save()
           return redirect('consultar_inventario')
       else:
           inventarioForm = InventarioForm()

    else:
        inventarioForm = InventarioForm()
    return render(request, "inventario/crear_inventario.html", {'inventarioForm': inventarioForm})


def eliminar_inventario(request):
    if request.method == "POST":
       inventarioForm = InventarioForm(request.POST)
       if inventarioForm.is_valid():
           inventarioForm.save()
           return redirect('consultar_inventario')
       else:
           inventarioForm = InventarioForm()

    else:
        inventarioForm = InventarioForm()
    return render(request, "inventario/eliminar_inventario.html", {'inventarioForm': inventarioForm})


def modificar_inventario(request):
    if request.method == "POST":
       inventarioForm = InventarioForm(request.POST)
       if inventarioForm.is_valid():
           inventarioForm.save()
           return redirect('consultar_inventario')
       else:
           inventarioForm = InventarioForm()

    else:
        inventarioForm = InventarioForm()
    return render(request, "inventario/modificar_inventario.html", {'inventarioForm': inventarioForm})


### CRUD PARA LA ENTIDAD OPCIONES
def consultar_opciones(request):
    if request.method == "POST":
       opcionesForm = OpcionesForm(request.POST)
       if opcionesForm.is_valid():
           opcionesForm.save()
           return redirect('consultar_opciones')
       else:
           opcionesForm = OpcionesForm()

    else:
        opcionesForm = OpcionesForm()
    return render(request, "opciones/consultar_opciones.html", {'opcionesForm': opcionesForm})


def crear_opciones(request):
    if request.method == "POST":
       opcionesForm = OpcionesForm(request.POST)
       if opcionesForm.is_valid():
           opcionesForm.save()
           return redirect('consultar_opciones')
       else:
           opcionesForm = OpcionesForm()

    else:
        opcionesForm = OpcionesForm()
    return render(request, "opciones/crear_opciones.html", {'opcionesForm': opcionesForm})



def eliminar_opciones(request):
    if request.method == "POST":
       opcionesForm = OpcionesForm(request.POST)
       if opcionesForm.is_valid():
           opcionesForm.save()
           return redirect('consultar_opciones')
       else:
           opcionesForm = OpcionesForm()

    else:
        opcionesForm = OpcionesForm()
    return render(request, "opciones/eliminar_opciones.html", {'opcionesForm': opcionesForm})



def modificar_opciones(request):
    if request.method == "POST":
       opcionesForm = OpcionesForm(request.POST)
       if opcionesForm.is_valid():
           opcionesForm.save()
           return redirect('consultar_opciones')
       else:
           opcionesForm = OpcionesForm()

    else:
        opcionesForm = OpcionesForm()
    return render(request, "opciones/modificar_opciones.html", {'opcionesForm': opcionesForm})



### CRUD PARA LA ENTIDAD PRODUCTO
def consultar_producto(request):
    if request.method == "POST":
       productoForm = ProductoForm(request.POST)
       if productoForm.is_valid():
           productoForm.save()
           return redirect('consultar_producto')
       else:
           productoForm = ProductoForm()

    else:
        productoForm = ProductoForm()
    return render(request, "producto/consultar_producto.html", {'productoForm': productoForm})



def crear_producto(request):
    if request.method == "POST":
       productoForm = ProductoForm(request.POST)
       if productoForm.is_valid():
           productoForm.save()
           return redirect('consultar_producto')
       else:
           productoForm = ProductoForm()

    else:
        productoForm = ProductoForm()
    return render(request, "producto/crear_producto.html", {'productoForm': productoForm})


def eliminar_producto(request):
    if request.method == "POST":
       productoForm = ProductoForm(request.POST)
       if productoForm.is_valid():
           productoForm.save()
           return redirect('consultar_producto')
       else:
           productoForm = ProductoForm()

    else:
        productoForm = ProductoForm()
    return render(request, "producto/eliminar_producto.html", {'productoForm': productoForm})


def modificar_producto(request):
    if request.method == "POST":
       productoForm = ProductoForm(request.POST)
       if productoForm.is_valid():
           productoForm.save()
           return redirect('consultar_producto')
       else:
           productoForm = ProductoForm()

    else:
        productoForm = ProductoForm()
    return render(request, "producto/modificar_producto.html", {'productoForm': productoForm})




### CRUD PARA LA ENTIDAD PROVEEDOR
def consultar_proveedor(request):
    if request.method == "POST":
       proveedorForm = ProveedorForm(request.POST)
       if proveedorForm.is_valid():
           proveedorForm.save()
           return redirect('consultar_proveedor')
       else:
           proveedorForm = ProveedorForm()

    else:
        proveedorForm = ProveedorForm()
    return render(request, "proveedor/consultar_proveedor.html", {'proveedorForm': proveedorForm})



def crear_proveedor(request):
    if request.method == "POST":
       proveedorForm = ProveedorForm(request.POST)
       if proveedorForm.is_valid():
           proveedorForm.save()
           return redirect('consultar_proveedor')
       else:
           proveedorForm = ProveedorForm()

    else:
        proveedorForm = ProveedorForm()
    return render(request, "proveedor/crear_proveedor.html", {'proveedorForm': proveedorForm})


def eliminar_proveedor(request):
    if request.method == "POST":
       proveedorForm = ProveedorForm(request.POST)
       if proveedorForm.is_valid():
           proveedorForm.save()
           return redirect('consultar_proveedor')
       else:
           proveedorForm = ProveedorForm()

    else:
        proveedorForm = ProveedorForm()
    return render(request, "proveedor/eliminar_proveedor.html", {'proveedorForm': proveedorForm})


def modificar_proveedor(request):
    if request.method == "POST":
       proveedorForm = ProveedorForm(request.POST)
       if proveedorForm.is_valid():
           proveedorForm.save()
           return redirect('consultar_proveedor')
       else:
           proveedorForm = ProveedorForm()

    else:
        proveedorForm = ProveedorForm()
    return render(request, "proveedor/modificar_proveedor.html", {'proveedorForm': proveedorForm})



### CRUD PARA LA ENTIDAD ROLES
def consultar_roles(request):
    if request.method == "POST":
       rolesForm = RolesForm(request.POST)
       if rolesForm.is_valid():
           rolesForm.save()
           return redirect('consultar_roles')
       else:
           rolesForm = RolesForm()

    else:
        rolesForm = RolesForm
    return render(request, "roles/consultar_roles.html", {'rolesForm': rolesForm})


def crear_roles(request):
    if request.method == "POST":
       rolesForm = RolesForm(request.POST)
       if rolesForm.is_valid():
           rolesForm.save()
           return redirect('consultar_roles')
       else:
           rolesForm = RolesForm()

    else:
        rolesForm = RolesForm
    return render(request, "roles/crear_roles.html", {'rolesForm': rolesForm})


def eliminar_roles(request):
    if request.method == "POST":
       rolesForm = RolesForm(request.POST)
       if rolesForm.is_valid():
           rolesForm.save()
           return redirect('consultar_roles')
       else:
           rolesForm = RolesForm()

    else:
        rolesForm = RolesForm
    return render(request, "roles/eliminar_roles.html", {'rolesForm': rolesForm})



def modificar_roles(request):
    if request.method == "POST":
       rolesForm = RolesForm(request.POST)
       if rolesForm.is_valid():
           rolesForm.save()
           return redirect('consultar_roles')
       else:
           rolesForm = RolesForm()

    else:
        rolesForm = RolesForm
    return render(request, "roles/modificar_roles.html", {'rolesForm': rolesForm})



### CRUD PARA LA ENTIDAD USUARIO_FACTURAS
def consultar_usuario_facturas(request):
    if request.method == "POST":
       usuario_facturasForm = Usuario_facturasForm(request.POST)
       if usuario_facturasForm.is_valid():
           usuario_facturasForm.save()
           return redirect('consultar_usuario_facturas')
       else:
           usuario_facturasForm = Usuario_facturasForm()

    else:
        usuario_facturasForm = Usuario_facturasForm
    return render(request, "usuario_facturas/consultar_usuario_facturas.html", {'usuario_facturasForm': usuario_facturasForm})



def crear_usuario_facturas(request):
    if request.method == "POST":
       usuario_facturasForm = Usuario_facturasForm(request.POST)
       if usuario_facturasForm.is_valid():
           usuario_facturasForm.save()
           return redirect('consultar_usuario_facturas')
       else:
           usuario_facturasForm = Usuario_facturasForm()

    else:
        usuario_facturasForm = Usuario_facturasForm()
    return render(request, "usuario_facturas/crear_usuario_facturas.html", {'usuario_facturasForm': usuario_facturasForm})



def eliminar_usuario_facturas(request):
    if request.method == "POST":
       usuario_facturasForm = Usuario_facturasForm(request.POST)
       if usuario_facturasForm.is_valid():
           usuario_facturasForm.save()
           return redirect('consultar_usuario_facturas')
       else:
           usuario_facturasForm = Usuario_facturasForm()

    else:
        usuario_facturasForm = Usuario_facturasForm
    return render(request, "usuario_facturas/eliminar_usuarios_facturas.html", {'usuario_facturasForm': usuario_facturasForm})



def modificar_usuario_facturas(request):
    if request.method == "POST":
       usuario_facturasForm = Usuario_facturasForm(request.POST)
       if usuario_facturasForm.is_valid():
           usuario_facturasForm.save()
           return redirect('consultar_usuario_facturas')
       else:
           usuario_facturasForm = Usuario_facturasForm()

    else:
        usuario_facturasForm = Usuario_facturasForm
    return render(request, "usuario_facturas/modificar_usuario_facturas.html", {'usuario_facturasForm': usuario_facturasForm})



### CRUD PARA LA ENTIDAD USUARIO_ROLES
def consultar_usuario_roles(request):
    if request.method == "POST":
       usuario_rolesForm = Usuario_rolesForm(request.POST)
       if usuario_rolesForm.is_valid():
           usuario_rolesForm.save()
           return redirect('consultar_usuario_roles')
       else:
           usuario_rolesForm = Usuario_rolesForm()

    else:
        usuario_rolesForm = Usuario_rolesForm
    return render(request, "usuario_roles/consultar_Usuario_roles.html", {'usuario_rolesForm': usuario_rolesForm})


def crear_usuario_roles(request):
    if request.method == "POST":
       usuario_rolesForm = Usuario_rolesForm(request.POST)
       if usuario_rolesForm.is_valid():
           usuario_rolesForm.save()
           return redirect('consultar_usuario_roles')
       else:
           usuario_rolesForm = Usuario_rolesForm()

    else:
        usuario_rolesForm = Usuario_rolesForm
    return render(request, "usuario_roles/crear_usuario_roles.html", {'usuario_rolesForm': usuario_rolesForm})


def eliminar_usuario_roles(request):
    if request.method == "POST":
       usuario_rolesForm = Usuario_rolesForm(request.POST)
       if usuario_rolesForm.is_valid():
           usuario_rolesForm.save()
           return redirect('consultar_usuario_roles')
       else:
           usuario_rolesForm = Usuario_rolesForm()

    else:
        usuario_rolesForm = Usuario_rolesForm
    return render(request, "usuario_roles/eliminar_usiuario_roles.html", {'usuario_rolesForm': usuario_rolesForm})



def modificar_usuario_roles(request):
    if request.method == "POST":
       usuario_rolesForm = Usuario_rolesForm(request.POST)
       if usuario_rolesForm.is_valid():
           usuario_rolesForm.save()
           return redirect('consultar_usuario_roles')
       else:
           usuario_rolesForm = Usuario_rolesForm()

    else:
        usuario_rolesForm = Usuario_rolesForm
    return render(request, "usuario_roles/modificar_usuario_roles.html", {'usuario_rolesForm': usuario_rolesForm})



### CRUD PARA LA ENTIDAD USUARIOS
def consultar_usuarios(request):
    if request.method == "POST":
       usuariosForm = UsuariosForm(request.POST)
       if usuariosForm.is_valid():
           usuariosForm.save()
           return redirect('consultar_usuarios')
       else:
           usuariosForm = UsuariosForm()

    else:
        usuariosForm = UsuariosForm
    return render(request, "usuarios/consultar_usuarios.html", {'usuariosForm': usuariosForm})



def crear_usuarios(request):
    if request.method == "POST":
       usuariosForm = UsuariosForm(request.POST)
       if usuariosForm.is_valid():
           usuariosForm.save()
           return redirect('consultar_usuarios')
       else:
           usuariosForm = UsuariosForm()

    else:
        usuariosForm = UsuariosForm
    return render(request, "usuarios/crear_usuarios.html", {'usuariosForm': usuariosForm})



def eliminar_usuarios(request):
    if request.method == "POST":
       usuariosForm = UsuariosForm(request.POST)
       if usuariosForm.is_valid():
           usuariosForm.save()
           return redirect('consultar_usuarios')
       else:
           usuariosForm = UsuariosForm()

    else:
        usuariosForm = UsuariosForm
    return render(request, "usuarios/eliminar_usuarios.html", {'usuariosForm': usuariosForm})


def modificar_usuarios(request):
    if request.method == "POST":
       usuariosForm = UsuariosForm(request.POST)
       if usuariosForm.is_valid():
           usuariosForm.save()
           return redirect('consultar_usuarios')
       else:
           usuariosForm = UsuariosForm()

    else:
        usuariosForm = UsuariosForm
    return render(request, "usuarios/modificar_usuarios.html", {'usuariosForm': usuariosForm})