# Generated by Django 3.1.4 on 2020-12-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketing_Products', '0013_auto_20201224_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='brochuresandflyers',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='customholidaycards',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='directmailpostcards',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='hangtags',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='labelsandstickers',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='ncrforms',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='postcards',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AddField(
            model_name='presentationfolders',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='Description',
            field=models.TextField(default='des', max_length=2048),
        ),
    ]
