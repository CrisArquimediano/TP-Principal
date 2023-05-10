# Generated by Django 4.2.1 on 2023-05-09 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_turno_taller_frecuencia_km_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno_taller',
            name='frecuencia_km',
            field=models.IntegerField(choices=[(5000, '5.000 KM'), (10000, '10.000 KM'), (15000, '15.000 KM'), (20000, '20.000 KM'), (25000, '25.000 KM'), (30000, '30.000 KM'), (35000, '35.000 KM'), (40000, '40.000 KM'), (45000, '45.000 KM'), (50000, '50.000 KM'), (55000, '55.000 KM'), (60000, '60.000 KM'), (65000, '65.000 KM'), (70000, '70.000 KM'), (75000, '75.000 KM'), (80000, '80.000 KM'), (85000, '85.000 KM'), (90000, '90.000 KM'), (95000, '95.000 KM'), (100000, '100.000 KM'), (105000, '105.000 KM'), (110000, '110.000 KM'), (115000, '115.000 KM'), (120000, '120.000 KM'), (125000, '125.000 KM'), (130000, '130.000 KM'), (135000, '135.000 KM'), (140000, '140.000 KM'), (145000, '145.000 KM'), (150000, '150.000 KM'), (155000, '155.000 KM'), (160000, '160.000 KM'), (165000, '165.000 KM'), (170000, '170.000 KM'), (175000, '175.000 KM'), (180000, '180.000 KM'), (185000, '185.000 KM'), (190000, '190.000 KM'), (195000, '195.000 KM'), (200000, '200.000 KM')], null=True, validators=[django.core.validators.MinValueValidator(5000), django.core.validators.MaxValueValidator(200000)]),
        ),
    ]
