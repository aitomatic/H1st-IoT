# Generated by Django 2.2.1 on 2019-05-20 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0105_auto_20190517_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalconfig',
            name='last_updated',
        ),
    ]
