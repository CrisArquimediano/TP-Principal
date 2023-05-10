# Generated by Django 4.2.1 on 2023-05-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0010_alter_turno_taller_estado_alter_turno_taller_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno_taller',
            name='estado',
            field=models.CharField(choices=[('rechazado', 'Rechazado'), ('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('terminado', 'Terminado')], default='en_proceso', max_length=10),
        ),
        migrations.AlterField(
            model_name='turno_taller',
            name='tipo',
            field=models.CharField(choices=[('service', 'Service'), ('evaluacion', 'Evaluacion'), ('extraordinario', 'Extraordinario'), ('reparacion', 'Reparacion')], default='service', max_length=14),
        ),
    ]
