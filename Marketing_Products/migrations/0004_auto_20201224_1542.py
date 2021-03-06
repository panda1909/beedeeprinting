# Generated by Django 3.1.4 on 2020-12-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketing_Products', '0003_quotationpostcards_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.RemoveField(
            model_name='quotationpostcards',
            name='templates',
        ),
        migrations.AddField(
            model_name='quotationpostcards',
            name='templates',
            field=models.ManyToManyField(to='Marketing_Products.Templates'),
        ),
    ]
