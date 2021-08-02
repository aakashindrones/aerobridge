# Generated by Django 3.2.5 on 2021-08-02 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcs_operations', '0036_alter_flightpermission_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightplan',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Specify Flight end date and time in Indian Standard Time (IST)'),
        ),
        migrations.AlterField(
            model_name='flightplan',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Specify Flight start date and time in Indian Standard Time (IST)'),
        ),
    ]
