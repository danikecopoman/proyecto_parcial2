# Generated by Django 4.1.3 on 2022-11-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0002_rename_estado_tipoplato_estado_activo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vianda',
            name='fecha_vianda',
            field=models.DateField(),
        ),
        migrations.RemoveField(
            model_name='vianda',
            name='tipo_plato',
        ),
        migrations.AddField(
            model_name='vianda',
            name='tipo_plato',
            field=models.ManyToManyField(to='vianda.tipoplato'),
        ),
    ]
