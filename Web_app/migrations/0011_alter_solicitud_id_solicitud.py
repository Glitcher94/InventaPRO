# Generated by Django 4.2.7 on 2023-11-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_app', '0010_solicitud_programa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='id_solicitud',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]