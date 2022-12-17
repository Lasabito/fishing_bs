def get_filters_count(context, query):
    fish_types = ['Сафрид', 'Чернокоп', 'Паламуд', 'Лефер', 'Попче', 'Зарган']
    locations = ['Eмине', 'Кокетрайс', 'Елените', 'Мегалката', 'Равда', 'Поморие',
                 'Ставрова', 'Канала', 'Чукалята', 'Атия', 'Таласакра', 'Созопол',
                 'Дюни', 'Маслен']
    for fish in fish_types:
        context[fish] = len(query.filter(fish_type=fish).all())
    for location in locations:
        context[location] = len(query.filter(location__contains=location).all())
    return context