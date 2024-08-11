# Generated by Django 5.0.6 on 2024-08-11 06:13

import market_place.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0002_alter_customuser_options_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default=5, upload_to=market_place.models.UniqueImageName()),
            preserve_default=False,
        ),
    ]
