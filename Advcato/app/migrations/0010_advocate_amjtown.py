# Generated by Django 5.0.6 on 2024-08-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_advocate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='amjtown',
            field=models.TextField(null=True),
        ),
    ]
