# Generated by Django 4.2.4 on 2023-09-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0015_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]