courses_dict = {
    'Экологичный быт': 'ecolife',
    'Осознанный гардероб': 'wardrobe',
    'Цифровой минимализм': 'digital'
}

courses = {
    'wardrobe': {
        0: {
            'title': 'День 0. Вступление.',
            'description': '''Первый материал - подготовительный. В нем я рассказываю о том, что такое осознанный 
            гардероб, о чем будет курс, какие сложности могут возникнуть при расхламлении и как делить вещи на 
            нужные и ненужные. После прочтения не забудь нажать на кнопку "Готово", чтобы завтра получить первое 
            задание!''',
            'url': 'https://nothing-extra.ru/wardrobe-intro/',
            'new': True
        },
        1: {
            'title': 'День 1. Диаграмма занятости',
            'description':'''Залог хорошего гардероба - это подбор вещей под ваш образ жизни. Иначе одежда будет 
            висеть в шкафу, вместо того чтобы гулять и жить вместе с нами. Поэтому первый шаг - это разобраться, 
            как мы проводим свое время, чтобы следующим шагом подобрать удобные и классные вещи под наш ритм и 
            интересы.''',
            'url': 'http://nothing-extra.ru/day1-diagram/',
            'new': True
        },
        2: {
            'title': 'День 2. Визуализация нашего стиля',
            'description': '''Время мы разбирались с тем, какая одежда нам нужна для комфортной жизни. А сегодня 
            давайте попробуем подобрать те визуальные образы и идеи, которые нам нравятся и которые мы хотим 
            видеть в своем гардеробе.''',
            'url': 'http://nothing-extra.ru/day2-visualization/',
            'new': True
        },
        3: {
            'title': 'День 3. Составляем план гардеробной капсулы',
            'description': '''Чтобы построить свой гардероб осознанно - всегда нужен план! Сегодняшний день посвятим 
            составлению этого плана: структуризируем наш гардероб и обозначим те вещи, которые составят его основу.   
                      ''',
            'url': 'http://nothing-extra.ru/day3-capsule-and-base/',
            'new': True
        },
        4: {
            'title': 'День 4. Куда отдать ненужное?',
            'description': '''Скорей всего, уже после составления плана вы вспомнили вещи, с которыми готовы 
            расстаться. Но можно ли расстаться с вещами экологично, не просто выбрасывая их в мусорку? Да! Давайте 
            сегодня посмотрим, куда мы можем деть все ненужное, чтобы эти вещи пригодились еще где-то.''',
            'url': 'http://nothing-extra.ru/day4-kuda-otdat/',
            'new': True
        },
        5: {
            'title': 'День 5. Разбираем средний слой',
            'description': '''Приступаем к исследованию шкафов! Начнем со среднего слоя - это вещи, которые чаще 
            всего мы подразумеваем под словом "одежда": брюки, платья, кофты, джемперы и прочее. Таких вещей обычно 
            довольно много, поэтому выделим на это задание два дня.''',
            'url': 'http://nothing-extra.ru/day5-6-middle-layer/',
            'new': True
        },
        6: {
            'title': 'День 6. Продолжаем со средним слоем',
            'description': '''Как и договаривались вчера, сегодня продолжаем разбирать средний слой. На всякий случай 
            дублирую ссылку на материал дня''',
            'url': 'http://nothing-extra.ru/day5-6-middle-layer/',
            'new': False
        },
        7: {
            'title': 'День 7. Воскресение',
            'description': '''Воскресение во всех мини-курсах - день отдыха от заданий, а материал дня совсем 
            короткий. Проведи этот день в свое удовольствие!''',
            'url': 'http://nothing-extra.ru/day7-wardrobe/',
            'new': True
        },
        8: {
            'title': 'День 8. Разбираем нижний слой',
            'description': '''Надеюсь, у тебя получилось хорошо отдохнуть вчера. Сегодня переходим от среднего слоя к 
            нижнему: это все наши носочки, чулочки, белье и подобные вещицы. Их не так много, но они мелкие, 
            поэтому уделим побольше времени хранению.''',
            'url': 'http://nothing-extra.ru/day8-underwear/',
            'new': True
        },
        9: {
            'title': 'День 9. Разбираем верхний слой и обувь',
            'description': '''От нижнего - к верхнему! И заодно посмотрим, что лежит на обувной полке. Эти две 
            категории вещей довольно удобно смотреть вместе - они обычно находятся рядом и дополняют друг друга в 
            образах.''',
            'url': 'http://nothing-extra.ru/day9-up-and-shoes/',
            'new': True
        },
        10: {
            'title': 'День 10. Последняя категория для разбора - аксессуары',
            'description': '''Сегодня заканчиваем с разбором. Как и в составлении образов, в последнюю очередь идут 
            аксессуары. Сюда относятся ювелирные украшения, часы, сумки, платки... У каждого человека свой набор 
            нужных аксессуаров. Какой будет у вас?)''',
            'url': 'http://nothing-extra.ru/day10-accessories/',
            'new': True
        },
        11: {
            'title': 'День 11. Наконец-то собираем капсулы',
            'description': '''Ура! Закончив с разбором, пора приступать к составлению гардероба-конструктора. Это не 
            быстрый процесс, поэтому предлагаю выделить два дня. Посоставлять образы, подумать, каких вещей не 
            хватает для комбинирования, а какие - наоборот, никуда не вписываются. Это еще один день, в который можно 
            уделить время комплексной оценке гардероба. Кстати, насколько он совпал с той теойтеоретической схемой, 
            которую составляли в третьем дне?''' ,
            'url': 'http://nothing-extra.ru/day11-12-capsules/',
            'new': True
        },
        12: {
            'title': 'День 12. Продолжаем собирать капсулы',
            'description': '''Как договаривались, сегодня продолжаем собирать капсулы. Хорошего тебе дня!
            ''',
            'url': 'http://nothing-extra.ru/day11-12-capsules/',
            'new': False
        },
        13: {
            'title': 'День 13. ',
            'description': '''Помнишь, в четвертом дне мы разбирались, куда можно отдать ненужное? Скорей всего после 
            разбора у тебя появились вещи, с которыми пора расстаться. Сегодня - день, когда нужно сказать им спасибо 
            и отправить дальше. А еще сегодня уделим время тем вещам, которые останутся с тобой, но с ними нужно 
            немного поработать: например, убрать катышки или отнести в ремонт. Кстати, это последнее практическое 
            задание!''',
            'url': 'http://nothing-extra.ru/day13-repair/',
            'new': True
        },
        14: {
            'title': 'День 14. Заключительный!',
            'description': '''Вот и последний, заключительный день! Спасибо тебе за проделанную работу! Надеюсь, 
            в этом мини-курсе нашлось что-то интересное и полезное. А может, он помог тебе выделить время на 
            упорядочение своего гардероба. Будет здорово, если оставишь небольшой отзыв. Напиши его, пожалуйста, 
            моему создателю: <a href='https://t.me/o_lyubimova'>. А я отправляю последний материал:''',
            'url': 'http://nothing-extra.ru/day14-finish/',
            'new': True
        }
    },
    'ecolife': {
        0: {
            'title': 'day0',
            'description': '''
            ''',
            'url': '',
            'new': True
        },
        1: {
            'title': 'day1',
            'description': '''
            ''',
            'url': 'http://nothing-extra.ru/part1-1-zero-waste/',
            'new': True
        },
        2: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-2-recycling-points/',
            'new': True
        },
        3: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-3-fridge/',
            'new': True
        },
        4: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-4-kitchen/',
            'new': True
        },
        5: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-5-packets/',
            'new': True
        },
        6: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-6-sweets/',
            'new': True
        },
        7: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-7-relax/',
            'new': True
        },
        8: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-mindfull-nutrition/',
            'new': True
        },
        9: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-organic-cosmetic/',
            'new': True
        },
        10: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-kosmetika-uhodi/',
            'new': True
        },
        11: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-decorative-cosmetic/',
            'new': True
        },
        12: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-chemistry/',
            'new': True
        },
        13: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-pharmacy/',
            'new': True
        },
        14: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/part1-relax-14/',
            'new': True
        }
    },
    'digital': {
        0: {
            'title': 'day0',
            'description': '''
            ''',
            'url': 'http://nothing-extra.ru/day0-digital-minimalism/',
            'new': True
        },
        1: {
            'title': 'day1',
            'description': '''
            ''',
            'url': 'https://nothing-extra.ru/day1-time/'
        },
        2: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day3-social-nets/'
        },
        3: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day3-social-nets/'
        },
        4: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day4-weakness-moments/'
        },
        5: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day5-calm-down/'
        },
        6: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day6-lent/'
        },
        7: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day7-email/'
        },
        8: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day8-messages/'
        },
        9: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day9-communication/'
        },
        10: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day10-gallery/'
        },
        11: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day11-apps-downloads/'
        },
        12: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day12-not-trash/'
        },
        13: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day13-boredom/'
        },
        14: {
            'title': 'day0',
            'description': '''
                            ''',
            'url': 'http://nothing-extra.ru/day14-peace/'
        }
    }
}


