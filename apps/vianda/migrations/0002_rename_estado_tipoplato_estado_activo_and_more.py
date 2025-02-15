# Generated by Django 4.1.3 on 2022-11-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoplato',
            old_name='estado',
            new_name='estado_activo',
        ),
        migrations.RemoveField(
            model_name='vianda',
            name='user',
        ),
        migrations.AlterField(
            model_name='vianda',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado')], max_length=11),
        ),
        migrations.AlterField(
            model_name='vianda',
            name='frecuencia',
            field=models.CharField(choices=[('semanal', 'Semanal'), ('quincenal', 'Quincenal')], max_length=11),
        ),
        migrations.AlterField(
            model_name='vianda',
            name='tipo_menu',
            field=models.CharField(choices=[('normal', 'Normal'), ('diabetico', 'Diabetico'), ('vegetariano', 'Vegetariano')], max_length=11),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Freceuncia',
        ),
        migrations.DeleteModel(
            name='TipoMenu',
        ),
    ]
