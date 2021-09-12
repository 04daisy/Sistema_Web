from django.db import models


# Create your models here.

class Bodega(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    observacion = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Bodega"

    def __str__(self):
        return "{}".format(self.descripcion)


class Categoria(models.Model):

    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    fecha = models.CharField(max_length=200)
    codigo = models.CharField(max_length=150)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Categoria"

    def __str__(self):
        return "{}{}{}".format(self.descripcion, " ", self.marca)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Ciudad"

    def __str__(self):
        return "{}".format(self.nombre)


class Detalle_factura(models.Model):
    cantidad = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100)
    valor = models.CharField(max_length=50)
    descuento = models.CharField(max_length=100)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Detalle_factura"

    def __str__(self):
        return "{}".format(self.descripcion)


class Estado_facturas(models.Model):
    tipo_estado = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Estado_facturas"


class Factura(models.Model):
    num_factura = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=200)
    iva = models.CharField(max_length=100)
    total = models.CharField(max_length=200)
    forma_pago = models.CharField(max_length=200)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Factura"


class Forma_pago(models.Model):
    tipo_pago = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100)
    num_tarjeta = models.CharField(max_length=200)
    banco = models.CharField(max_length=100)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Forma_pago"


class Inventario(models.Model):
    descripcion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=200)
    producto = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    fecha = models.CharField(max_length=250)
    bodega = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Inventario"


class Opciones(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Opciones"


class Producto(models.Model):

    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    marca = models.CharField(max_length=50)
    subtotal = models.CharField(max_length=10)
    iva = models.CharField(max_length=20)
    total = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Producto"
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return "{}".format(self.descripcion)


class Proveedor(models.Model):
    codigo = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Proveedor"


class Roles(models.Model):
    descripcion = models.CharField(max_length=50)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Roles"


class Usuario_facturas(models.Model):
    factura = models.CharField(max_length=10)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Usuario_facturas"


class Usuario_roles(models.Model):
    usuarios = models.CharField(max_length=10)
    roles = models.CharField(max_length=100)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Usuario_roles"


class Usuarios(models.Model):
    nombres = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=250)
    contrasenia = models.CharField(max_length=20)
    estado_U = models.CharField(max_length=10)
    fecha = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "Usuarios"
