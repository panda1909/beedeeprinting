# Generated by Django 3.1 on 2021-02-03 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Cards', '0020_auto_20210203_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raised_ink_business_cards_price',
            name='US_Standard_Size',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
