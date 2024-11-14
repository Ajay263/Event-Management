# Generated by Django 4.0.2 on 2024-11-14 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(help_text='Subtitle for the about section', max_length=255)),
                ('description', models.TextField(help_text='Main description of the about section (use paragraphs separated by \\n).')),
                ('image', models.ImageField(help_text='Upload an image for the about section.', upload_to='about_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('stop_time', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QRCodeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Stat number (e.g., 300+)', max_length=50)),
                ('text', models.CharField(help_text="Stat description (e.g., 'Participants')", max_length=100)),
                ('about_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='Events.aboutsection')),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BarcodeScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_time', models.DateTimeField()),
                ('time_taken', models.CharField(blank=True, max_length=15, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['time_taken'],
            },
        ),
        migrations.AddIndex(
            model_name='barcodescan',
            index=models.Index(fields=['time_taken'], name='Events_barc_time_ta_f13b68_idx'),
        ),
    ]
