# Generated by Django 4.0.2 on 2024-08-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='stop_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
