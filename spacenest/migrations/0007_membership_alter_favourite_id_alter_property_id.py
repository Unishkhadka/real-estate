# Generated by Django 5.0.2 on 2024-03-14 17:21

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacenest', '0006_alter_favourite_id_alter_property_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('listing_count', models.IntegerField(default=0)),
            ],
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
