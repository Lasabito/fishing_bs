from django.db import models


class ChooseTownModel(models.Model):
    CHOICES = (
        ('atiya', 'Атия'),
        ('burgas', 'Бургас'),
        ('nesebar', 'Несебър'),
        ('pomorie', 'Поморие'),
        ('ravda', 'Равда'),
        ('sozopol', 'Созопол'),
        ('chernomorets', 'Черноморец'),
    )
    town = models.CharField(
        max_length=15,
        choices=CHOICES,
    )
