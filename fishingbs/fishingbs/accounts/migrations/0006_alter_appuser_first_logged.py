# Generated by Django 4.1.3 on 2022-12-12 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_logged',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
