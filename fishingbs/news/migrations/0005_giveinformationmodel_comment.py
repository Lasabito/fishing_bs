# Generated by Django 4.1.3 on 2022-12-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_created_giveinformationmodel_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveinformationmodel',
            name='comment',
            field=models.TextField(default='None', max_length=1500),
            preserve_default=False,
        ),
    ]
