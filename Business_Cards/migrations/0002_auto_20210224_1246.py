# Generated by Django 3.1 on 2021-02-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '__first__'),
        ('Business_Cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business_cards_price',
            name='Template',
        ),
        migrations.AddField(
            model_name='business_cards_price',
            name='Template_ref',
            field=models.ManyToManyField(to='core.Designguide'),
        ),
    ]
