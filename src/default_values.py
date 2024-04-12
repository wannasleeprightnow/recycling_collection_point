import uuid

default_commands_values = [
    {
        "id": uuid.uuid4(),
        "input_text": "/start",
        "output_text": 'Привет!\n\
С помощью данного чат-бота ты сможешь максимально быстро узнавать актуальную \
информацию о деятельности пункта приема вторсырья "Птичка".\n\
Более подробно ты сможешь ознакомиться с функционалом бота с помощью кнопки \
"Помощь".'
        },
    {
        "id": uuid.uuid4(),
        "input_text": "График работы.",
        "output_text": """
<b>Пр. Набережный, 5 стр. 2:</b>
Вт, Чт, Пт: 14:00 – 19:00
Сб, Вс.: 11:00 – 16:00
Пн, Ср.: выходной

<b>Ул. 30 лет Победы, 21/3:</b>
Ср, Чт: 14:00 – 19:00
Сб, Вс: 10:00 – 15:00
Пн, Вт, Пт: выходной

<b>Ул. Фармана Салманова, 2:</b>
Вт, Чт, Пт: 14:00 – 19:00
Сб, Вс.: 11:00 – 16:00
Пн, Ср.: выходной
        """
        },
    {
        "id": uuid.uuid4(),
        "input_text": "Есть ли вознаграждение за сданное вторсырье?",
        "output_text": "Рады сообщить, что раз в несколько месяцев в пунктах \
приема вторсырья будут запускаться акции по сбору определенной фракции, \
за которую можно будет получить баллы, а баллы обменять на приятные \
подарки!\n\nС 13 апреля по 31 мая в пункте приема вторсырья по адресу: \
ул. Фармана Салманова, 2 будет действовать акция на фракцию «1 ПЭТ (бутылки)\
»Подробнее следить за акцией можно на странице «Птички»: \
https://vk.com/ptichka_punkt \n\nИ ЕЩЕ! Очень важно, что благотворительный \
проект « С заботой о старшем поколении» (помощь одиноким людям в виде \
продуктов, средств личной гигиены и прочих нужд) реализуется на регулярной \
основе благодаря посетителям экологического проекта АО «Полигон-ЛТД» - \
пунктов приема вторсырья «Птичка» и жителями, которые складывают крышечки в \
Чудо-деревья."
        },
    {
        "id": uuid.uuid4(),
        "input_text": "Сотрудничество",
        "output_text": "Почта для направления письма с Вашим предложением:\
info@poligonltd.ru"
        },
    {
        "id": uuid.uuid4(),
        "input_text": "По номеру телефона/в группе Вконтакте",
        "output_text": "Номер телефона пунктов: 89322484552 (общая линия, \
отвечает менеджер эко-проектов в рабочее время)\nГруппа Вконтакте:\
https://vk.com/ptichka_punkt"
        },
    ]

default_events_values = [
    {"id": uuid.uuid4(),
     "title": "СВОП",
     "event_description": "Обмен хорошими, но ненужными вещами. Это отличный \
способ подарить ненужным вещам нового хозяина и самому найти то, что может \
точно пригодиться! Когда проходят? Стараемся проводить один раз в месяц.\n\
<a href='https://vk.com/ptichka_punkt?w=wall-216486932_967'>Посмотреть пример \
мероприятия</a>",
},
    {"id": uuid.uuid4(),
     "title": "Мастер - классы",
     "event_description": "В рамках наших СВОПов и других мероприятий обычно \
проходят различные интересные мастер-классы, такие как: роспись одежды, \
роспись деревянных значков, создание картин из вторсырья и т.п.\n\
<a href='https://vk.com/ptichka_punkt?w=wall-216486932_917'>Посмотреть пример \
мероприятия</a>",
},
    {"id": uuid.uuid4(),
     "title": "Эко-уроки",
     "event_description": "Эко-уроки проводим преимущественно в \
образовательных учреждениях, включает в себя знакомство с нашим пунктом, \
процессом сбора и сортировки вторсырья, информация о существующих фракциях и \
какие принимаем именно мы и т.п. Когда проходят? Можем провести по запросу, а \
также в рамках других эко-мероприятий.\n\
<a href='https://vk.com/ptichka_punkt?w=wall-216486932_984'>Посмотреть пример \
мероприятия</a>",
},
    {"id": uuid.uuid4(),
     "title": "Обмен книгами",
     "event_description": "Буккроссинг — на территории пунктов у нас \
существует обмен книгами, можно принести свои ненужные книги и забрать себе \
приглянувшиеся. Нередко получается найти нашему посетителю что-то интересное \
для чтения!",
},
    {"id": uuid.uuid4(),
     "title": "Благотворительность",
     "event_description": "Каждый месяц мы собираем продуктовые наборы и \
средства личной гигиены и доставляем одиноким пожилым людям совместно с \
центром поддержки семей «Круг надежд».Организовываем сборы для животных \
приютов корма, амуниции и всех необходимостей, а также проводим акцию \
«Елки,щепа, добрые дела», в рамках которых собираем елки после нового года и \
делаем из них щепу, которую перенаправляем ботаническому саду (для утепления \
растений зимой и т.п.), животным приютам (для настила в вольерах и т.п): \
<a href='https://vk.com/ptichka_punkt?w=wall-216486932_923'>Посмотреть пример \
мероприятия</a>\n\
<a href='https://vk.com/ptichka_punkt?w=wall-216486932_1030'>Посмотреть пример \
мероприятия</a>\n\
<a href='https://vk.com/ptichka_punkt?w=wall-216486932_1000'>Посмотреть пример \
мероприятия</a>",
},
    {"id": uuid.uuid4(),
     "title": "Еще",
     "event_description": "Наша деятельность очень обширна, мы стараемся \
создавать много всего интересного и полезного! Акции, конкурсы, различные \
сборы, полезная информация из мира экологии все это можно найти в нашей \
<a href='https://vk.com/ptichka_punkt'>группе Вконтакте</a> и \
<a href='https://t.me/ptichka_punkt'>Телеграм-канале</a>. Не упустите \
много всего классного вместе с «Птичкой»!"
},
]
