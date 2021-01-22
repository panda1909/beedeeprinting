# Generated by Django 3.1.4 on 2021-01-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210120_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Printing', 'Printing'), ('Dispatched', 'Dispatched'), ('Delivered', 'Delivered'), ('Designing', 'Design Undergoing')], max_length=256),
        ),
    ]