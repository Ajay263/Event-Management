# Generated by Django 4.0.2 on 2024-04-19 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barcodescan',
            name='barcode_data',
        ),
    ]
