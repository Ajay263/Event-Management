# Generated by Django 4.0.2 on 2024-08-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_event_stop_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcodescan',
            name='scan_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='barcodescan',
            name='time_taken',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
