# Generated by Django 4.0.6 on 2022-07-14 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atencion',
            old_name='id',
            new_name='patente',
        ),
    ]
