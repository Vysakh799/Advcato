# Generated by Django 5.0.6 on 2024-08-17 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_langauges_aname_remove_langauges_english_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='langauges',
            old_name='languages',
            new_name='language',
        ),
    ]