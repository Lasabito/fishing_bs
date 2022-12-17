def get_max_length_of_a_sequence(sequence):
    result = 0
    for k in sequence:
        for v in k:
            if len(v) > result:
                result = len(v)
    return result


def get_locations():
    locations = (
        ('atiya', 'Атия'),
        ('diuni', 'Дюни'),
        ('elenite', 'Елените'),
        ('emine', 'Емине'),
        ('kanala', 'Канала'),
        ('koketrais', 'Кокетрайс'),
        ('maslen-nos', 'Маслен нос'),
        ('megalkata', 'Мегалката'),
        ('pomorie', 'Поморие'),
        ('ravda', 'Равда'),
        ('sozopol', 'Созопол'),
        ('stavrova-banka', 'Ставрова банка'),
        ('talasakra', 'Таласакра'),
        ('chukalqta', 'Чукалята'),
    )
    return locations


def get_fish_types():
    result = (
        ('Сафрид', 'Сафрид'),
        ('Чернокоп', 'Чернокоп'),
        ('Паламуд', 'Паламуд'),
        ('Лефер', 'Лефер'),
        ('Попче', 'Попче'),
        ('Зарган', 'Зарган'),
    )
    return result


def get_intensities():
    result = (
        ('Малка', 'Малка'),
        ('Средна', 'Средна'),
        ('Голяма', 'Голяма'),
    )
    return result


def get_catching_types():
    result = (
        ('Тролинг', 'Тролинг'),
        ('Чипаре', 'Чипаре'),
    )
    return result


def get_locations_for_news():
    locations = (
        ('Атия', 'Атия'),
        ('Дюни', 'Дюни'),
        ('Елените', 'Елените'),
        ('Емине', 'Емине'),
        ('Канала', 'Канала'),
        ('Кокетрайс', 'Кокетрайс'),
        ('Маслен нос', 'Маслен нос'),
        ('Мегалката', 'Мегалката'),
        ('Поморие', 'Поморие'),
        ('Равда', 'Равда'),
        ('Созопол', 'Созопол'),
        ('Ставрова банка', 'Ставрова банка'),
        ('Таласакра', 'Таласакра'),
        ('Чукалята', 'Чукалята'),
    )
    return locations
