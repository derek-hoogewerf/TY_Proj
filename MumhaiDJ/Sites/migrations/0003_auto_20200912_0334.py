# Generated by Django 3.0.3 on 2020-09-11 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sites', '0002_auto_20200912_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='c_time',
        ),
        migrations.RemoveField(
            model_name='site',
            name='o_time',
        ),
    ]
