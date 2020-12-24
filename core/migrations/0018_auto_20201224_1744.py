# Generated by Django 3.1.4 on 2020-12-24 17:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20201224_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Product_name',
            field=models.CharField(default='pd', max_length=512),
        ),
        migrations.AddField(
            model_name='orders',
            name='Template',
            field=models.ImageField(default=datetime.datetime(2020, 12, 24, 17, 44, 35, 739831, tzinfo=utc), max_length=256, upload_to='static/Order_templates'),
            preserve_default=False,
        ),
    ]
