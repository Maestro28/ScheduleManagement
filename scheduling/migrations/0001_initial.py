# Generated by Django 4.0.5 on 2022-06-25 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(editable=False)),
                ('end_datetime', models.DateTimeField(editable=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='scheduling.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('duration', models.DurationField(help_text='duration of the procedure')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='accounting.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_datetime', models.DateTimeField(editable=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.procedure')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
