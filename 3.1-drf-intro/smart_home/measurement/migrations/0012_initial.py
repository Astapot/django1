# Generated by Django 4.2.4 on 2023-09-01 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('measurement', '0011_delete_measurement_delete_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('sensorid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
        ),
    ]
