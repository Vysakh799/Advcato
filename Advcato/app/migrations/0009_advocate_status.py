# Generated by Django 5.0.6 on 2024-08-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_cases_chat_parties'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
