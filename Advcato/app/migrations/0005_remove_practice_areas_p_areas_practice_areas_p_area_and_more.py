# Generated by Django 5.0.6 on 2024-08-16 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_practice_areas_admiralty_and_maritime_law_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice_areas',
            name='p_areas',
        ),
        migrations.AddField(
            model_name='practice_areas',
            name='p_area',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Selected_parea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.advocate')),
                ('p_area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.practice_areas')),
            ],
        ),
    ]