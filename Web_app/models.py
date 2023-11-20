# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MovimientosInventario(models.Model):
    id_movimiento = models.FloatField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=50, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud', blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'movimientos_inventario'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=20, blank=True, null=True)
    orden_compra = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)


    class Meta:
        db_table = 'producto'


class Solicitud(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    tipo_solicitud = models.CharField(max_length=20, blank=True, null=True)
    estado_solicitud = models.CharField(max_length=20, blank=True, null=True)
    beneficiario = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'solicitud'


def pin_validator(value):
    if not value.isdigit() or len(value) != 5:
        raise ValidationError('El PIN debe contener exactamente 5 dígitos.')


class Usuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255, blank=True, null=True)
    correo = models.EmailField(unique=True, max_length=30, blank=True, null=True)
    clave = models.CharField(max_length=255, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)

    objects = BaseUserManager()

    def __str__(self):
        return self.nombre_usuario  # O el campo que prefieras mostrar como representación de cadena

    class Meta:
        db_table = 'usuario'




class DetalleSolicitud(models.Model):
    id_detalle_sol = models.FloatField(primary_key=True)
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad_solicitada = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'detalle_solicitud'
