# Generated by Django 4.2.4 on 2023-09-01 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_alter_measurement_sensorid_alter_sensor_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
    ]
