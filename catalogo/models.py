from django.db import models

# Create your models here.

class Categoria(models.Model):
    """
    Modelo que representa una categoria de artículo (herramienta, accesorios, etc.).
    """
    nombre = models.CharField(max_length=200, help_text="Ingrese el nombre de la categoria (p. ej. herramienta, accesorios, etc.)")
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nombre

class Proveedor(models.Model):
    """
    Modelo que representa a un proveedor
    """
    nombreComp = models.CharField(max_length=100)
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('prov-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.nombreComp)

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Producto(models.Model):
    """
    Modelo que representa un producto (pero no una unidad específica).
    """

    nombre = models.CharField(max_length=200)

    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un producto tiene un solo proveedor, pero el mismo proveedor puede proveer muchos productos.
    # 'Proveedor' es un string, en vez de un objeto, porque la clase Proveedor aún no ha sido declarada.
    
    claveProducto = models.CharField(max_length=13)

    categoria = models.ManyToManyField(Categoria, help_text="Seleccione una categoria para este producto")
    # ManyToManyField, porque una categoria puede contener muchos productos y un producto puede cubrir varias categorias.
    # La clase Categoria ya ha sido definida, entonces podemos especificar el objeto arriba.
    
    def __str__(self):
        """
        String que representa al objeto Producto
        """
        return self.nombre
    
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('product-detail', args=[str(self.id)])

import uuid # Requerida para las instancias de libros únicos

class DetalleProducto(models.Model):
    """
    Modelo que representa.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este")
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True) 
    descuento = models.FloatField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Estatus del producto')      

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.producto.nombre)
