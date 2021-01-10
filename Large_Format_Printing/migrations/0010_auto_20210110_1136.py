# Generated by Django 3.1.4 on 2021-01-10 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Large_Format_Printing', '0009_auto_20210109_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foamcoreposters',
            name='Eighteen_By_TwentyFour',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='18" x 24" Cost'),
        ),
        migrations.AlterField(
            model_name='foamcoreposters',
            name='FourtySix_By_FourtyEight',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='46" x 48" Cost'),
        ),
        migrations.AlterField(
            model_name='foamcoreposters',
            name='ThirtySix_By_FourtyEight',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='36" x 48" Cost'),
        ),
        migrations.AlterField(
            model_name='foamcoreposters',
            name='Twelve_By_Eighteen',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='12" x 18" Cost'),
        ),
        migrations.AlterField(
            model_name='foamcoreposters',
            name='TwentyFour_By_ThirtySix',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='24" x 36" Cost'),
        ),
        migrations.AlterField(
            model_name='foamcoreposters',
            name='TwentyFour_By_TwentyFour',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='24" x 24" Cost'),
        ),
        migrations.AlterField(
            model_name='foamcoreposters',
            name='Twenty_By_Thrity',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='20" x 30" Cost'),
        ),
    ]