# Generated by Django 3.1 on 2021-02-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Cards', '0018_auto_20210201_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raised_spot_uv_business_cards_price',
            name='US_Standard_size',
            field=models.CharField(blank=True, max_length=555),
        ),
    ]