# Generated by Django 3.1.4 on 2021-01-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='Message',
            field=models.TextField(max_length=5000),
        ),
    ]