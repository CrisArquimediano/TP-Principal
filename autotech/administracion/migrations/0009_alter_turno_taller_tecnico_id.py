# Generated by Django 4.2.1 on 2023-05-09 00:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_alter_turno_taller_frecuencia_km'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno_taller',
            name='tecnico_id',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
    ]