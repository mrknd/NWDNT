# Generated by Django 3.2 on 2025-01-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroller', '0012_auto_20240806_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='stroller',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
