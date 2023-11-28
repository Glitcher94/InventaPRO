# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import BaseUserManager


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

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
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class MovimientosInventario(models.Model):
    id_movimiento = models.BigIntegerField(primary_key=True)
    tipo_movimiento = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos_inventario'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    categoria = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    estado = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    orden_compra = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Solicitud(models.Model):
    id_solicitud = models.CharField(primary_key=True, max_length=10, db_collation='Modern_Spanish_CI_AS')
    fecha_solicitud = models.DateField(blank=True, null=True)
    estado_solicitud = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    tipo_solicitud = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    beneficiario = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    programa = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_usuario, correo, clave, rol):
        # Validaciones y lógica de creación de usuario
        # ...

        user = self.model(
            nombre_usuario=nombre_usuario,
            correo=correo,
            clave=clave,
            rol=rol,
        )
        user.save(using=self._db)
        return user

class Usuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    correo = models.EmailField(unique=True, max_length=30)
    clave = models.CharField(max_length=255)
    rol = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['nombre_usuario', 'clave', 'rol']

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'  # Campo que se usa para el login

    def __str__(self):
        return self.nombre_usuario
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
    
    def get_username(self):
        return self.correo
