# Generated by Django 2.2.10 on 2021-02-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_tipo_salida_de_campo_color2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_salida_de_campo',
            name='requerimientos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]