# Generated by Django 3.1.4 on 2020-12-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Cards', '0002_auto_20201224_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_cards_price',
            name='Template',
            field=models.ImageField(max_length=256, null=True, upload_to='static/Business_Cards_Templates'),
        ),
    ]