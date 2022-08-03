from django.db import models
# third-party
from model_utils.models import TimeStampedModel
# Django
from django.db import models
# local
from .managers import ProductManager


class Marca(TimeStampedModel):
    """
        Representa las marcas de productos
    """
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name
    

class Provider(TimeStampedModel):
    """
    Proveedores de productos
    """
    name = models.CharField('Razón Social', max_length=100)
    email = models.EmailField('Email', blank=True, null=True)
    phone = models.CharField('Telefono', max_length=40, blank=True)
    web = models.URLField('sitio Web', blank=True)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.name
    
    
class Product(TimeStampedModel):
    """
        Representa los productos
    """
    UNIT_CHOISE = (
        ('0', 'kilogramos'),
        ('1', 'litros'),
        ('2', 'unidad'),
    )
    barcode = models.CharField('Codigo de Barras', max_length=13, unique=True)
    name = models.CharField('Nombre', max_length=40)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Proveedor')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')
    due_date = models.DateField('Fecha de Vencimiento', blank=True, null=True)
    description=models.TextField('Descripcion de producto', blank=True)
    unit = models.CharField('Unidad de medida', max_length=1, choices=UNIT_CHOISE)
    count = models.PositiveIntegerField('Cantidad en el almacen', default=0)
    purchase_price = models.DecimalField('Precio de compra', max_digits=7, decimal_places=2)
    sale_price = models.DecimalField('Precio de venta', max_digits=7, decimal_places=2)
    num_sale = models.PositiveIntegerField('Cantidad de ventas', default=0)
    anulate = models.BooleanField('eliminado', default=False)

    objects = ProductManager()
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

