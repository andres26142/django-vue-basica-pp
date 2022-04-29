from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Campos del modelo Cliente"""
    nom_cliente = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre Cliente",
        help_text="Nombre del cliente")
    estado = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Estado",
        help_text="Estado")

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # Nombre del modelo
        verbose_name = "Cliente"
        # Nombre del modelo en plural
        verbose_name_plural = "Cliente"

    def __str__(self):
        return self.nom_cliente


class Articulo(models.Model):
    """Campos del modelo Articulo"""
    nom_articulo = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre del Artículo",
        help_text="Nombre del artículo")
    precio = models.FloatField(
        null=False, blank=False,
        verbose_name="Precio del Artículo",
        help_text="Precio del artículo")    

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # Nombre del modelo
        verbose_name = "Artículo"
        # Nombre del modelo en plural
        verbose_name_plural = "Artículo"
        
    def __str__(self):
        return self.nom_articulo
        
        
class Orden(models.Model):
    """Campos del modelo Orden"""
    fecha = models.DateField(
        verbose_name="Fecha de la Orden",
        help_text="Fecha de la orden")
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING,
        verbose_name="Cliente",
        help_text="Cliente")

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # Nombre del modelo
        verbose_name = "Orden"
        # Nombre del modelo en plural
        verbose_name_plural = "Orden"
        
    def __str__(self):
        return str(self.fecha) + ": " + str(self.cliente)
        
        
class ArticuloOrden(models.Model):
    """Campos del modelo ArticuloOrden"""
    cant = models.PositiveIntegerField(
        null=False, blank=False, default=0,
        verbose_name="Cantidad del Artículo",
        help_text="Cantidad del artículo")
    articulo = models.ForeignKey(
        Articulo, on_delete=models.DO_NOTHING,
        verbose_name="Artículo",
        help_text="Artículo")
    orden = models.ForeignKey(
        Orden, on_delete=models.DO_NOTHING,
        verbose_name="Orden",
        help_text="Orden")

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # Constraint, no se puede repetir
        unique_together = ('articulo', 'orden')
        # Nombre del modelo
        verbose_name = "Artículo Orden"
        # Nombre del modelo en plural
        verbose_name_plural = "Artículo Orden"
        
    def __str__(self):
        return str(self.orden) + ": " + str(self.articulo)