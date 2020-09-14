# Generated by Django 3.0.3 on 2020-09-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='rating',
        ),
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.CharField(choices=[('C1', 'Category 1'), ('C2', 'Category 2'), ('C3', 'Category 3'), ('C4', 'Category 4'), ('C5', 'Category 5'), ('C6', 'Category 6'), ('C7', 'Category 7'), ('C8', 'Category 8')], max_length=2),
        ),
        migrations.AlterField(
            model_name='site',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]