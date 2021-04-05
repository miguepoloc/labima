# Generated by Django 2.2.10 on 2021-04-05 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20210405_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo_Variable',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('variable', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='estacion',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Tipo_Estacion'),
        ),
    ]
