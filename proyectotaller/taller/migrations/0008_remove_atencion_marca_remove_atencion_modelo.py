# Generated by Django 4.0.6 on 2022-07-14 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0007_alter_atencion_descripcion_alter_atencion_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencion',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='atencion',
            name='modelo',
        ),
    ]
