# Generated by Django 4.2.1 on 2023-05-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_alter_service_id_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_extraordinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tasks', models.JSONField()),
                ('id_turno', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='administracion.turno_taller')),
            ],
        ),
        migrations.RemoveField(
            model_name='registro_reparacion',
            name='id_registro',
        ),
        migrations.RemoveField(
            model_name='registro_reparacion',
            name='tasks',
        ),
        migrations.AddField(
            model_name='registro_reparacion',
            name='origen',
            field=models.TextField(blank=True, choices=[('evaluacion', 'Evaluacion'), ('extraordinario', 'Extraordinario')], null=True),
        ),
        migrations.AddField(
            model_name='registro_reparacion',
            name='tasks_hechas',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registro_reparacion',
            name='tasks_pendientes',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro_reparacion',
            name='id_turno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='administracion.turno_taller'),
        ),
        migrations.DeleteModel(
            name='Checklist_reparacion',
        ),
    ]
