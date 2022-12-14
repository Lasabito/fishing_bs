# Generated by Django 4.1.3 on 2022-12-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchInFishingAreaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('atiya', 'Атия'), ('diuni', 'Дюни'), ('elenite', 'Елените'), ('emine', 'Емине'), ('kanala', 'Канала'), ('koketrais', 'Кокетрайс'), ('maslen-nos', 'Маслен'), ('megalkata', 'Мегалката'), ('pomorie', 'Поморие'), ('ravda', 'Равда'), ('sozopol', 'Созопол'), ('stavrova-banka', 'Ставрова банка'), ('talasakra', 'Таласакра'), ('chukalqta', 'Чукалята')], max_length=20)),
            ],
        ),
    ]
