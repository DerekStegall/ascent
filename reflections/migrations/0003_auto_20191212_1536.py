# Generated by Django 3.0 on 2019-12-12 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reflections', '0002_auto_20191209_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reflection',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
