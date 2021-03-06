# Generated by Django 3.0.3 on 2020-02-26 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('number', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('AV', 'Available'), ('UA', 'Unavailable'), ('BA', 'Banned')], default='AV', max_length=2)),
                ('rating', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('number', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('AV', 'Available'), ('UA', 'Unavailable'), ('BA', 'Banned')], default='AV', max_length=2)),
                ('license', models.CharField(max_length=10)),
                ('rating', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('number', models.PositiveSmallIntegerField()),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('econ_name', models.CharField(blank=True, max_length=25, verbose_name='Emergency Contact Name')),
                ('econ_num', models.PositiveSmallIntegerField(blank=True, verbose_name='Emergency Contact Number')),
                ('status', models.CharField(choices=[('FR', 'Free'), ('BK', 'Booked'), ('PP', 'Payment Pending')], default='FR', max_length=2)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
