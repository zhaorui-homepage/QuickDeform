# Generated by Django 2.0.5 on 2018-06-14 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okada', '0002_auto_20180414_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earthquake',
            name='Magnitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='earthquake',
            name='Moment',
            field=models.FloatField(),
        ),
    ]