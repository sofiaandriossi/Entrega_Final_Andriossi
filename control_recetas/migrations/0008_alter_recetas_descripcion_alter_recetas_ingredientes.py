# Generated by Django 4.2.7 on 2023-11-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_recetas', '0007_recetas_creador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='descripcion',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='ingredientes',
            field=models.CharField(max_length=1000),
        ),
    ]