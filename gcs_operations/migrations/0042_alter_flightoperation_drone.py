# Generated by Django 3.2.7 on 2021-09-24 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0051_auto_20210623_1241'),
        ('gcs_operations', '0041_auto_20210901_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightoperation',
            name='drone',
            field=models.ForeignKey(help_text='Pick the drone that will be used to fly this opreation', on_delete=django.db.models.deletion.CASCADE, to='registry.aircraft'),
        ),
    ]