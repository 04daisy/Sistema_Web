from django import forms
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

###--------------------------------------

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['descripcion', 'fecha', 'observacion',]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'marca', 'fecha', 'codigo',]


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'fecha',]


class Detalle_facturaForm(forms.ModelForm):
    class Meta:
        model = Detalle_factura
        fields = ['cantidad', 'descripcion', 'valor', 'descuento', 'fecha',]


class Estado_facturasForm(forms.ModelForm):
    class Meta:
        model = Estado_facturas
        fields = ['tipo_estado', 'descripcion', 'fecha',]


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['num_factura', 'descripcion', 'subtotal', 'iva', 'total', 'forma_pago', 'fecha',]


class Forma_pagoForm(forms.ModelForm):
    class Meta:
        model = Forma_pago
        fields = ['tipo_pago', 'descripcion', 'num_tarjeta', 'banco', 'fecha', ]


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['descripcion', 'ciudad', 'producto', 'cantidad', 'fecha', 'bodega', ]



class OpcionesForm(forms.ModelForm):
    class Meta:
        model = Opciones
        fields = ['descripcion', 'fecha', ]



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [ 'codigo', 'descripcion', 'marca', 'subtotal', 'iva', 'total', 'categoria',]



class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['codigo', 'nombre_empresa', 'descripcion', 'fecha',]


class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['descripcion', 'fecha',]



class Usuario_facturasForm(forms.ModelForm):
    class Meta:
        model = Usuario_facturas
        fields = ['factura',]



class Usuario_rolesForm(forms.ModelForm):
    class Meta:
        model = Usuario_roles
        fields = ['usuarios', 'roles', 'fecha',]


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'direccion', 'usuario', 'contrasenia', 'estado_U', 'fecha',]