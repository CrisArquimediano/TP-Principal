# Generated by Django 4.2.1 on 2023-05-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_registro_extraordinario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_extraordinario',
            name='detalle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registro_reparacion',
            name='detalle_evaluacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]