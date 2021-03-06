from .emoji import emoji


courses_dict = {
    'Экологичный быт': 'ecolife',
    'Осознанный гардероб': 'wardrobe',
    'Цифровой минимализм': 'digital'
}

courses_dict_reverse = {
    'ecolife': 'Экологичный быт',
    'wardrobe': 'Осознанный гардероб',
    'digital': 'Цифровой минимализм'
}

courses = {
    'ecolife': {
        0: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 0. Вступление' + '</strong>',
            'description': '''Первый материал - вводный. В нем я расскажу о том, чем будем заниматься целых 14 дней, какие сложности могут возникнуть при расхламлении и как делить вещи на нужные и ненужные. После прочтения не забудь нажать на кнопку "Готово", чтобы завтра получить первое задание!'''
                           + emoji.get('raising_hands'),
            'url': 'http://nothing-extra.ru/foreword/',
            'need_answer': True
        },
        1: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 1. Про концепцию Zero Waste' + '</strong>',
            'description': '''Сегодня предлагаю познакомиться с концепцией нулевых отходов и разобраться, почему экологичный образ жизни - это совсем не про переработку. Переработка стоит аж на четвертом месте из пяти! Давайте посмотрим, какие еще там есть пункты и какие из них подходят вашему образу жизни'''
                           + emoji.get("hug"),
            'url': 'http://nothing-extra.ru/part1-1-zero-waste/',
            'need_answer': True
        },
        2: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 2. Куда сдать вторсырье?' + '</strong>',
            'description': '''Каждый день каждый из нас генерирует мусор. Точнее, мы привыкли думать об этих вещах как о мусоре - пластиковой упаковке, стеклянных бутылках, треснувших тарелках и прочем. Но многим из этих вещей можно дать вторую жизнь, продлить их жизненный цикл. Сегодня посмотрим, что и куда можно отнести, чтобы уменьшить свой мусорный след. И чтобы это был не другой конец города!'''
                           + emoji.get('love_you_gesture'),
            'url': 'http://nothing-extra.ru/part1-2-recycling-points/',
            'need_answer': True
        },
        3: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 3. Холодильник' + '</strong>',
            'description': '''Поиск ненужного начнем с холодильника. Нам не понадобятся сегодня советы по организации пространства, но вечер может стать полным открытий. Может быть вы найдете старый новый соус, может быть замороженные ягоды, а может быть просто отметите, что вместо тетрапака молока можно брать поллитровую бутылочку. Давайте скорее заглянем внутрь!'''
                           + emoji.get('hearts_face'),
            'url': 'http://nothing-extra.ru/part1-3-fridge/',
            'need_answer': True
        },
        4: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 4. Еда вне холодильника' + '</strong>',
            'description': '''Разобравшись с холодильником, можно приступать к более многочисленным шкафчикам. Там тоже может быть много интересного! Кроме разбора, сегодня также уделим время организации хранения. Ведь чаще всего мы теряем продукты просто потому что они очень редко попадаются нам на глаза. Давайте попробуем это исправить ''' + emoji.get('upside_down_face'),
            'url': 'http://nothing-extra.ru/part1-4-kitchen/',
            'need_answer': True
        },
        5: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 5. Пакеты с пакетами' + '</strong>',
            'description': '''Сегодня займемся внедрением более экологичного подхода к использованию пластиковых пакетов и пакетиков. И заодно разберем все те, которые уже накопились ''' + emoji.get('shopping_bags'),
            'url': 'http://nothing-extra.ru/part1-5-packets/',
            'need_answer': True
        },
        6: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 6. Готовимся идти в магазин' + '</strong>',
            'description': '''Одна из самых главных заповедей экологичной жизни - это не покупать лишние вещи. Те самые, которые полежат без дела и потом просто отправятся в мусорку. К ним относятся и сами покупки, и то, что идет в довесок - упаковка. Сегодня посмотрим, что может уберечь нас от ненужных покупок и попробуем применить эти советы на практике '''
                           + emoji.get('biceps'),
            'url': 'http://nothing-extra.ru/part1-6-sweets/',
            'need_answer': True
        },
        7: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 7. Выходной!' + '</strong>',
            'description': '''В каждом деле залог успеха не столько в том, чтобы усердно трудиться, но и в том, чтобы хорошо отдыхать. Давайте сегодня отдохнем! Выделите время и займитесь тем, чем давно хотели заняться '''
                           + emoji.get('relieved_face'),
            'url': 'http://nothing-extra.ru/part1-7-relax/',
            'need_answer': True
        },
        8: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 8. Осознаннное питание' + '</strong>',
            'description': '''Едим мы с вами каждый день, но далеко не каждый раз получаем от еды удовольствие. Давайте попробуем повысить наш уровень счастья - за счет более осознанного подхода к питанию. Ни слова про калории и витамины. Зато несколько слов о планировании, чтобы не расстраиваться, выкидывая еду. И немного идей интуитивного питания '''
                           + emoji.get('winking_face'),
            'url': 'http://nothing-extra.ru/part1-mindfull-nutrition/',
            'need_answer': True
        },
        9: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 9. Натуральная косметика' + '</strong>',
            'description': '''Кроме еды внутрь мы употребляем еще и косметику. Ну как внутрь - мажем на себя, а она через кожу проникает внутрь. А часть мы смываем водой, и эти остатки уплывают вместе с водой  обратно в природу. Так что еще один шаг к более экологичному потреблению - это выбрать более экологичную косметику. Давайте сегодня посмотрим, какие вообще виды косметики бывают'''
                           + emoji.get('hug'),
            'url': 'http://nothing-extra.ru/part1-organic-cosmetic/',
            'need_answer': True
        },
        10: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 10. Косметика для ухода' + '</strong>',
            'description': '''Вчера читали, сегодня давай разбирать наши запасы. Возьмем только часть уходовой косметики - это всякие шампуни, крема и гигиенические помады. Кучка должна получиться не очень большая, поэтому часть времени потратим на удобную организацию хранения. Будет несколько интересных советов '''
                           + emoji.get('winking_face'),
            'url': 'http://nothing-extra.ru/part1-kosmetika-uhodi/',
            'need_answer': True
        },
        11: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 11. Декоративная косметика' + '</strong>',
            'description': '''Сегодня - вторая часть косметики. Для парней сегодняшний день не очень актуальный, зато у девушек может быть насыщенным. Разбираем косметичку! '''
                           + emoji.get('lipstick'),
            'url': 'http://nothing-extra.ru/part1-decorative-cosmetic/',
            'need_answer': True
        },
        12: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 12. Бытовая химия' + '</strong>',
            'description': '''Последняя часть, которую с натяжкой, но можно отнести к косметике - бытовая химия. Всякие порошки, чистящие средства и прочее. Они тоже могут быть органическими и экологичными. И, кстати, при этом могут остаться недорогими '''
                           + emoji.get('raising_hands'),
            'url': 'http://nothing-extra.ru/part1-chemistry/',
            'need_answer': True
        },
        13: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 13. Предпоследний - аптечка' + '</strong>',
            'description': '''Добавить экологичности можно и в наши взаимоотношения с лекарствами. Лечиться все так же будем проверенными лекарствами, но постараемся генерировать поменьше мусора. Будьте здоровы!'''
                           + emoji.get('biceps'),
            'url': 'http://nothing-extra.ru/part1-pharmacy/',
            'need_answer': True
        },
        14: {
            'title':  '<strong>' +  emoji.get('calendar') + ' День 14. Мы на финише!' + '</strong>',
            'description': '''Вот и заключительный день нашего небольшого курса. Спасибо за все выполненные задания, за стремление к более экологичному образу жизни и за доверие '''
                           + emoji.get('heart') + ''' Надеюсь, часть советов пригодится вам в дальнейшем '''
                           + emoji.get('hug') + ''' Будет здорово, если оставите небольшой отзыв. Напишите его, пожалуйста, моему создателю: <a href='https://t.me/o_lyubimova'>@o.lyubimova</a>. А пока - ловите заключительный материал ''' + emoji.get('down_arrow'),
            'url': 'http://nothing-extra.ru/part1-relax-14/',
            'need_answer': True
        }
    },
    'wardrobe': {
        0: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 0. Вступление' + '</strong>',
            'description': '''Первый материал - подготовительный. В нем я рассказываю о том, что такое осознанный гардероб, о чем будет курс, какие сложности могут возникнуть при расхламлении и как делить вещи на нужные и ненужные. После прочтения не забудьте нажать на кнопку "Готово", чтобы завтра получить первое задание!'''
                           + emoji.get('raising_hands'),
            'url': 'https://nothing-extra.ru/wardrobe-intro/',
            'need_answer': True
        },
        1: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 1. Диаграмма занятости' + '</strong>',
            'description': '''Залог хорошего гардероба - это подбор вещей под ваш образ жизни. Иначе одежда будет висеть в шкафу, вместо того чтобы гулять и жить вместе с нами. Поэтому первый шаг - это разобраться, как мы проводим свое время, чтобы следующим шагом подобрать удобные и классные вещи под наш ритм и интересы'''
                           + emoji.get('upside_down_face'),
            'url': 'http://nothing-extra.ru/day1-diagram/',
            'need_answer': True
        },
        2: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 2. Визуализация нашего стиля' + '</strong>',
            'description': '''Время мы разбирались с тем, какая одежда нам нужна для комфортной жизни. А сегодня давайте попробуем подобрать те визуальные образы и идеи, которые нам нравятся и которые мы хотим видеть в своем гардеробе '''
                           + emoji.get('biceps'),
            'url': 'http://nothing-extra.ru/day2-visualization/',
            'need_answer': True
        },
        3: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 3. Составляем план гардеробной капсулы' + '</strong>',
            'description': '''Чтобы построить свой гардероб осознанно - всегда нужен план! Сегодняшний день посвятим составлению этого плана: структуризируем наш гардероб и обозначим те вещи, которые составят его основу '''
                           + emoji.get('heart_eyes_face'),
            'url': 'http://nothing-extra.ru/day3-capsule-and-base/',
            'need_answer': True
        },
        4: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 4. Куда отдать ненужное?' + '</strong>',
            'description': '''Скорей всего, уже после составления плана вы вспомнили вещи, с которыми готовы расстаться. Но можно ли расстаться с вещами экологично, не просто выбрасывая их в мусорку? Да! Давайте сегодня посмотрим, куда мы можем деть все ненужное, чтобы эти вещи пригодились еще где-то '''
                           + emoji.get('victory_hand'),
            'url': 'http://nothing-extra.ru/day4-kuda-otdat/',
            'need_answer': True
        },
        5: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 5. Разбираем средний слой' + '</strong>',
            'description': '''Приступаем к исследованию шкафов! Начнем со среднего слоя - это вещи, которые чаще всего мы подразумеваем под словом "одежда": брюки, платья, кофты, джемперы и прочее. Таких вещей обычно довольно много, поэтому выделим на это задание два дня '''
                           + emoji.get('t_shirt'),
            'url': 'http://nothing-extra.ru/day5-6-middle-layer/',
            'need_answer': False
        },
        6: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 6. Продолжаем со средним слоем' + '</strong>',
            'description': '''Как и договаривались вчера, сегодня продолжаем разбирать средний слой. На всякий случай дублирую ссылку на материал дня '''
                           + emoji.get('jeans'),
            'url': 'http://nothing-extra.ru/day5-6-middle-layer/',
            'need_answer': True
        },
        7: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 7. Выходной' + '</strong>',
            'description': '''Всегда должен быть выходной! Во всех мини-курсах - это седьмой день, день отдыха от заданий, а материал дня совсем короткий. Проведи этот день в свое удовольствие!'''
                           + emoji.get('relaxed_face'),
            'url': 'http://nothing-extra.ru/day7-wardrobe/',
            'need_answer': True
        },
        8: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 8. Разбираем нижний слой' + '</strong>',
            'description': '''Надеюсь, у тебя получилось хорошо отдохнуть вчера. Сегодня переходим от среднего слоя к нижнему: это все наши носочки, чулочки, белье и подобные вещицы. Их не так много, но они мелкие, поэтому уделим побольше времени хранению '''
                           + emoji.get('bikini'),
            'url': 'http://nothing-extra.ru/day8-underwear/',
            'need_answer': True
        },
        9: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 9. Разбираем верхний слой и обувь' + '</strong>',
            'description': '''От нижнего - к верхнему! И заодно посмотрим, что лежит на обувной полке. Эти две категории вещей довольно удобно смотреть вместе - они обычно находятся рядом и дополняют друг друга в образах '''
                           + emoji.get('boots'),
            'url': 'http://nothing-extra.ru/day9-up-and-shoes/',
            'need_answer': True
        },
        10: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 10. Последняя категория для разбора - аксессуары'
                      + '</strong>',
            'description': '''Сегодня заканчиваем с разбором. Как и в составлении образов, в последнюю очередь идут аксессуары. Сюда относятся ювелирные украшения, часы, сумки, платки... У каждого человека свой набор нужных аксессуаров. Какой будет у вас?) '''
                           + emoji.get('sunglasses'),
            'url': 'http://nothing-extra.ru/day10-accessories/',
            'need_answer': True
        },
        11: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 11. Наконец-то собираем капсулы' + '</strong>',
            'description': '''Ура! Закончив с разбором, пора приступать к составлению гардероба-конструктора. Это не быстрый процесс, поэтому предлагаю выделить два дня. Посоставлять образы, подумать, каких вещей не хватает для комбинирования, а какие - наоборот, никуда не вписываются. Это еще один день, в который можно уделить время комплексной оценке гардероба. Кстати, насколько он совпал с той теотеоретической схемой, которую составляли в третьем дне? '''
                           + emoji.get('raised_eyebrow'),
            'url': 'http://nothing-extra.ru/day11-12-capsules/',
            'need_answer': False
        },
        12: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 12. Продолжаем собирать капсулы' + '</strong>',
            'description': '''Как договаривались, сегодня продолжаем собирать капсулы. Хорошего тебе дня!'''
                           + emoji.get('relieved_face'),
            'url': 'http://nothing-extra.ru/day11-12-capsules/',
            'need_answer': True
        },
        13: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 13. Относим ненужное, чиним нужное' + '</strong>',
            'description': '''Помнишь, в четвертом дне мы разбирались, куда можно отдать ненужное? Скорей всего после разбора у тебя появились вещи, с которыми пора расстаться. Сегодня - день, когда нужно сказать им спасибо и отправить дальше. А еще сегодня уделим время тем вещам, которые останутся с тобой, но с ними нужно немного поработать: например, убрать катышки или отнести в ремонт. Кстати, это последнее практическое задание! '''
                           + emoji.get('winking_face'),
            'url': 'http://nothing-extra.ru/day13-repair/',
            'need_answer': True
        },
        14: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 14. Заключительный!' + '</strong>',
            'description': '''Вот и последний, заключительный день! ''' + emoji.get('party_popper') +
                           '''Спасибо тебе за проделанную работу! Надеюсь, в этом мини-курсе нашлось что-то интересное и полезное. А может, он помог тебе выделить время на упорядочение своего гардероба. Будет здорово, если оставишь небольшой отзыв. Напиши его, пожалуйста, <a href='https://t.me/o_lyubimova'>моему создателю </a> '''
                           + emoji.get('heart') +
                           ''' А я отправляю последний материал:''',
            'url': 'http://nothing-extra.ru/day14-finish/',
            'need_answer': True
        }
    },
    'digital': {
        0: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 0. Цифровой минимализм' + '</strong>',
            'description': '''Первый материал - вводный. В нем я расскажу о том, что будем подразумевать под цифровым минимализмом и чем будем заниматься целых 14 дней. После прочтения не забудь нажать на кнопку "Готово", чтобы завтра получить первое задание! '''
                           + emoji.get('raising_hands'),
            'url': 'http://nothing-extra.ru/day0-digital-minimalism/',
            'need_answer': True
        },
        1: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 1. Куда девается время?' + '</strong>',
            'description': '''Время - самый ценный ресурс, который у нас есть. Просто потому что он не восполняется. Тем не менее, мы все мастера по трате времени на занятия, которые не считаем ценными. Давайте попробуем разобраться, какие же занятия полезны, какие - лишние, и как вообще построен наш день. '''
                           + emoji.get('watch'),
            'url': 'https://nothing-extra.ru/day1-time/',
            'need_answer': True
        },
        2: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 2. Наши привычки' + '</strong>',
            'description': '''Они бывают полезные и не очень. Некоторые из них требуют усилия по поддержанию, а некоторые - прилипают так, что не отлепишь. Сегодня взглянем со стороны на наши обычные, привычные действия и подумаем, какие из них нам нравятся, а какие - не очень. Постарайтесь быть беспристрастными и ни в коем случае не занимайтесь самобичеванием ''' + emoji.get('smilling_face'),
            'url': 'http://nothing-extra.ru/day-2-habits/',
            'need_answer': True
        },
        3: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 3. Социальные сети' + '</strong>',
            'description': '''И сети они не только потому что связывают людей друг с другом, но и потому что в них очень легко попасть и запутаться. Давайте сегодня потратим немного времени, чтобы разобраться, как можно более осознанно использовать этот инструмент. Вместо того, чтобы он использовал нас '''
                           + emoji.get('fishing_pole'),
            'url': 'http://nothing-extra.ru/day3-social-nets/',
            'need_answer': True
        },
        4: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 4. Моменты слабости' + '</strong>',
            'description': '''А у вас бывают моменты слабости? Не очень понятно, о чем идет речь?) Открывайте новый материал, там и про моменты слабости - и про то, как с ними можно бороться '''
                           + emoji.get('biceps'),
            'url': 'http://nothing-extra.ru/day4-weakness-moments/',
            'need_answer': True
        },
        5: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 5. Еще немного про осознанность' + '</strong>',
            'description': '''Сегодня предложу вам пару практик осознанности. Звучит намного пафосней, чем на самом деле, но я правда считаю эти упражнения полезными. Будет здорово, если вы попробуете их '''
                           + emoji.get('relaxed_face'),
            'url': 'http://nothing-extra.ru/day5-calm-down/',
            'need_answer': True
        },
        6: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 6. Разбираемся с бесконечной лентой' + '</strong>',
            'description': '''... чтобы она стала конечной и максимально интересной. Помните ситуации, когда потратили много времени на скроллинг, но не увидели ничего полезного или хотя бы прикольного? Самое время повысить качество нашего пребывания в соцсетях! '''
                           + emoji.get('upside_down_face'),
            'url': 'http://nothing-extra.ru/day6-lent/',
            'need_answer': True
        },
        7: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 7. Электронная почта' + '</strong>',
            'description': '''Сколько у вас электронных ящиков? Почему именно столько? Получается ли следить за порядком в них? Каким образом это можно делать? Давайте сегодня поразбираемся с ответами на эти вопросы'''
                           + emoji.get('postbox'),
            'url': 'http://nothing-extra.ru/day7-email/',
            'need_answer': True
        },
        8: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 8. Мессенджеры' + '</strong>',
            'description': '''Говорить о мессенджерах особо нечего. Но в них тоже нужно навести порядок. Займемся этим!'''
                           + emoji.get('memo'),
            'url': 'http://nothing-extra.ru/day8-messages/',
            'need_answer': True
        },
        9: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 9. Новые грани общения' + '</strong>',
            'description': '''Спойлер: в конце сегодняшнего материала вас ждет необычное задание. Готовы? '''
                           + emoji.get('winking_face'),
            'url': 'http://nothing-extra.ru/day9-communication/',
            'need_answer': True
        },
        10: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 10. Фотогаллерея' + '</strong>',
            'description': '''Если вы любите фотографировать, то сегодняшнее задание может занять больше времени, чем предыдущие. Но выполнив его, вы удивитесь, сколько места вы освободили на своем смартфоне и тому, какой он все же шустрый '''
                           + emoji.get('victory_hand'),
            'url': 'http://nothing-extra.ru/day10-gallery/',
            'need_answer': True
        },
        11: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 11. Приложения, загрузки, экраны' + '</strong>',
            'description': '''Снова удаляем все ненужное! Давайте скорее приступим ''' + emoji.get('star_eyes_face'),
            'url': 'http://nothing-extra.ru/day11-apps-downloads/',
            'need_answer': True
        },
        12: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 12. Немного о том, куда выкидывать ненужное'
                      + '</strong>',
            'description': '''Ненужное, поломанное, устаревшее. Постарайтесь не выкидывать просто в мусорку. Куда тогда выкидывать? Открывайте материал, будем разбираться! '''
                           + emoji.get('wastebasket'),
            'url': 'http://nothing-extra.ru/day12-not-trash/',
            'need_answer': True
        },
        13: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 13. Не скучайте!' + '</strong>',
            'description': '''Хотя нет, немного поскучайте! Сегодняшний материал о пользе скуки, ничегонеделании (в прямом смысле) и вдохновении. Отдыхая, отдыхайте! ''' + emoji.get('upside_down_face'),
            'url': 'http://nothing-extra.ru/day13-boredom/',
            'need_answer': True
        },
        14: {
            'title':  '<strong>' + emoji.get('calendar') + ' День 14. Заключение' + emoji.get('party_popper')
                      + '</strong>',
            'description': '''Спасибо вам за прохождение этого небольшого курса о цифровом минимализме ''' +
                           emoji.get('heart') + '''' Надеюсь, вам понравилось и было интересно! Сегодня предлагаю немного порефлексировать и подумать, что из предложенных советов хочется применять и  дальше.  Будет здорово, если оставите небольшой отзыв. Напишите его, пожалуйста, в личные сообщения <a href='https://t.me/o_lyubimova'>@o.lubimova</a>. А вот и последний материал:''',
            'url': 'http://nothing-extra.ru/day14-peace/',
            'need_answer': True
        }
    }
}


