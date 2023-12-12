# Generated by Django 4.2.7 on 2023-12-11 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web_app', '0011_movimientosinventario_id_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientosinventario',
            name='id_usuario',
            field=models.ForeignKey(blank=True, db_column='id_usuario', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
