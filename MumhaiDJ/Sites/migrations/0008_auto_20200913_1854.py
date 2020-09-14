# Generated by Django 3.0.3 on 2020-09-13 13:24

import Sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sites', '0007_auto_20200913_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(validators=[Sites.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='droploc',
            field=models.TextField(verbose_name='Drop Location'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pickloc',
            field=models.TextField(verbose_name='Pick Up Location'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('P', 'Pending Confirmation'), ('B', 'Booked'), ('I', 'In Progress'), ('C', 'Completed'), ('R', 'Removed')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.CharField(choices=[('C0', 'Other'), ('C1', 'Adventure'), ('C2', 'Historical'), ('C3', 'Urban'), ('C4', 'Educational'), ('C5', 'Nature'), ('C6', 'Event Based')], default='C0', max_length=2),
        ),
        migrations.AlterField(
            model_name='site',
            name='img',
            field=models.ImageField(default='def_site.jpg', upload_to='site_pics', verbose_name='Site Image'),
        ),
        migrations.AlterField(
            model_name='site',
            name='number',
            field=models.CharField(max_length=10, verbose_name='Contact Number'),
        ),
    ]
