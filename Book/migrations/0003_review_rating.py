# Generated by Django 4.2.5 on 2023-11-17 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_book_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.RegexValidator(message='Rating must be between 1 and 5.', regex='^[1-5]$')]),
            preserve_default=False,
        ),
    ]
