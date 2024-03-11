# Generated by Django 5.0.2 on 2024-03-11 13:14

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacenest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, default='property/default.png', null=True, upload_to='property/', verbose_name='Property Image'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
