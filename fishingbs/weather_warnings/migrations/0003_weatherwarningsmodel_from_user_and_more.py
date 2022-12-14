# Generated by Django 4.1.3 on 2022-12-14 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_appuser_first_logged'),
        ('weather_warnings', '0002_rename_weatherswarningmodel_weatherwarningsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherwarningsmodel',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='weatherwarningsmodel',
            name='comment',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]