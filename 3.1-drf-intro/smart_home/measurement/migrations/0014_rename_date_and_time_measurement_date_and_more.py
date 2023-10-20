# Generated by Django 4.2.4 on 2023-09-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0013_alter_measurement_sensorid_alter_sensor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='date_and_time',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='measurement',
            old_name='sensorid',
            new_name='sensor',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]