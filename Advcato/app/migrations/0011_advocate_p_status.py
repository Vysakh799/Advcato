# Generated by Django 5.0.6 on 2024-08-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_advocate_amjtown'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='p_status',
            field=models.BooleanField(default=False),
        ),
    ]