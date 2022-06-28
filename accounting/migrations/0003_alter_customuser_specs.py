# Generated by Django 4.0.5 on 2022-06-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='specs',
            field=models.ManyToManyField(blank=True, related_name='users', to='accounting.specialization'),
        ),
    ]
