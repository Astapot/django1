# Generated by Django 4.2.4 on 2023-09-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.IntegerField(),
        ),
    ]