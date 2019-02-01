# Generated by Django 2.1.5 on 2019-02-01 17:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0084_equipmentuniquetypegroupmonitoreddatafieldconfig_highly_correlated_numeric_equipment_data_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='lowly_correlated_numeric_equipment_data_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
        migrations.RemoveField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='auto_included_numeric_equipment_data_fields',
        ),
        migrations.AddField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='auto_included_numeric_equipment_data_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
        migrations.RemoveField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='highly_correlated_numeric_equipment_data_fields',
        ),
        migrations.AddField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='highly_correlated_numeric_equipment_data_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
    ]
