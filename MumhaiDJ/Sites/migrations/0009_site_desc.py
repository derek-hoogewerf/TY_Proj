# Generated by Django 3.0.3 on 2020-09-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sites', '0008_auto_20200913_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='desc',
            field=models.TextField(default='Site_Desc', max_length=250),
        ),
    ]
