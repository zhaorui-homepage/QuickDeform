# Generated by Django 2.0.5 on 2018-07-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okada', '0003_auto_20180614_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Etitle', models.CharField(max_length=50)),
                ('Edatetime', models.CharField(max_length=50)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Magnitude', models.FloatField()),
                ('Depth', models.FloatField()),
                ('Strike1', models.FloatField()),
                ('Dip1', models.FloatField()),
                ('Rake1', models.FloatField()),
                ('Strike2', models.FloatField()),
                ('Dip2', models.FloatField()),
                ('Rake2', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='earthquake',
        ),
    ]
