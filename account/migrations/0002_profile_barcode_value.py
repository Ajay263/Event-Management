# Generated by Django 4.0.2 on 2024-04-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='barcode_value',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
