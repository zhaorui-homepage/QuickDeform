# Generated by Django 2.0.4 on 2018-04-14 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('okada', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='earthquake',
            old_name='Datetime',
            new_name='Edatetime',
        ),
        migrations.RenameField(
            model_name='earthquake',
            old_name='Title',
            new_name='Etitle',
        ),
    ]
