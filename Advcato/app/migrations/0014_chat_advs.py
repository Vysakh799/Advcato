# Generated by Django 5.0.6 on 2024-10-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_read_status_chat_advread_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='advs',
            field=models.BooleanField(default=False),
        ),
    ]