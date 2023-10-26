# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DetalleSolicitud(models.Model):
    id_detalle_sol = models.FloatField(primary_key=True)
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad_solicitada = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'detalle_solicitud'


class MovimientosInventario(models.Model):
    id_movimiento = models.FloatField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    id_usuario = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'movimientos_inventario'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'producto'


class Solicitud(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    id_usuario = models.BigIntegerField(blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    estado_solicitud = models.CharField(max_length=20, blank=True, null=True)
    ruta_archivo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'solicitud'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(unique=True, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'usuario'
