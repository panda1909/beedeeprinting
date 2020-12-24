# Generated by Django 3.1.4 on 2020-12-24 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20201224_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Delivery_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 24, 17, 57, 2, 290684, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerdata',
            name='Cell',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='customerdata',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
