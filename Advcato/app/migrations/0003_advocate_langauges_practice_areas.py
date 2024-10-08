# Generated by Django 5.0.6 on 2024-08-13 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_ucnfpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.TextField()),
                ('aphone', models.TextField()),
                ('aemail', models.TextField()),
                ('apassword', models.TextField()),
                ('aaddress', models.TextField()),
                ('aprofile', models.FileField(null=True, upload_to='')),
                ('agender', models.TextField(null=True)),
                ('bcr_no', models.TextField(null=True)),
                ('aheighest_qual', models.TextField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('idproof', models.FileField(null=True, upload_to='')),
                ('bc_certificate', models.FileField(null=True, upload_to='')),
                ('exp_certificate', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Langauges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malayalam', models.BooleanField(default=False)),
                ('english', models.BooleanField(default=False)),
                ('hindi', models.BooleanField(default=False)),
                ('aname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='Practice_areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_law', models.BooleanField(default=False)),
                ('civil_right_law', models.BooleanField(default=False)),
                ('family_law', models.BooleanField(default=False)),
                ('corporate_law', models.BooleanField(default=False)),
                ('intelectual_property_law', models.BooleanField(default=False)),
                ('employment_law', models.BooleanField(default=False)),
                ('personal_injury_law', models.BooleanField(default=False)),
                ('real_estate_law', models.BooleanField(default=False)),
                ('estate_planing_and_probate_law', models.BooleanField(default=False)),
                ('environmental_law', models.BooleanField(default=False)),
                ('bankruptcy_law', models.BooleanField(default=False)),
                ('immigration_law', models.BooleanField(default=False)),
                ('healthcare_law', models.BooleanField(default=False)),
                ('tax_law', models.BooleanField(default=False)),
                ('admiralty_and_maritime_law', models.BooleanField(default=False)),
                ('entertainment_law', models.BooleanField(default=False)),
                ('aname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.advocate')),
            ],
        ),
    ]
