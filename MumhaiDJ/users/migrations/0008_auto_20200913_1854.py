# Generated by Django 3.0.3 on 2020-09-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profiletry',
            name='user',
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='User First Name', max_length=25),
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Guide',
        ),
        migrations.DeleteModel(
            name='ProfileTry',
        ),
    ]
