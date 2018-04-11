# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0005_auto_20180103_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentUniqueTypeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('equipment_general_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_unique_type_groups', related_query_name='equipment_unique_type_group', to='Arimo_IoT_DataAdmin_Base.EquipmentGeneralType')),
                ('equipment_unique_types', models.ManyToManyField(blank=True, related_name='equipment_unique_type_groups', related_query_name='equipment_unique_type_group', to='Arimo_IoT_DataAdmin_Base.EquipmentUniqueType')),
            ],
            options={
                'ordering': ('equipment_general_type', 'name'),
            },
        ),
        migrations.AddField(
            model_name='equipmentuniquetype',
            name='groups',
            field=models.ManyToManyField(blank=True, to='Arimo_IoT_DataAdmin_Base.EquipmentUniqueTypeGroup'),
        ),
    ]
