# Generated by Django 3.1.4 on 2020-12-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketing_Products', '0006_auto_20201224_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates',
            name='file',
            field=models.FileField(max_length=256, upload_to="static/[('PostCards/', 'PostCards'), ('QuotationPostCards/', 'QuotationPostCards'), ('BrochuresAndFlyers/', 'BrochuresAndFlyers'), ('DirectMailPostCards/', 'DirectMailPostCards'), ('QuotationDirectMailPostCards/', 'QuotationDirectMailPostCards'), ('Calendars/', 'Calendars'), ('HangTags/', 'HangTags'), ('LabelsAndStickers/', 'LabelsAndStickers'), ('NCRForms/', 'NCRForms'), ('PresentationFolders/', 'PresentationFolders'), ('CustomHolidayCards/', 'CustomHolidayCards')]"),
        ),
    ]
