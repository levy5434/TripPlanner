# Generated by Django 3.1.1 on 2020-09-28 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TripPlannerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='trip',
            name='no_of_days',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
