# Generated by Django 5.0.6 on 2024-08-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0004_item_category_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('equipment', 'Equipment'), ('crop', 'Crop'), ('fertilizer', 'Fertilizer'), ('pesticides', 'Pesticides'), ('other', 'Other')], max_length=255, null=True),
        ),
    ]
