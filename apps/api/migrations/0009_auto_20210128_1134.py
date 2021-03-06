# Generated by Django 2.2.10 on 2021-01-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210128_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='componentes',
            field=models.ManyToManyField(blank=True, help_text='Seleccione los componentes de la estación', null=True, to='api.Componente_Estacion'),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='sensores',
            field=models.ManyToManyField(blank=True, help_text='Seleccione los sensores de la estación', null=True, to='api.Sensor_Estacion'),
        ),
    ]
