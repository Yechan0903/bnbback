# Generated by Django 5.1 on 2024-08-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_price_per_night_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price_per_night',
            field=models.PositiveIntegerField(help_text='Positive Numbers Only', verbose_name='Price'),
        ),
    ]
