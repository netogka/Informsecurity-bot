import telebot
from telebot import types
bot = telebot.TeleBot("ТОКЕН")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Привет, {0.first_name}, я помощник, предназначенный для обучения по теме \"Информационная безопасность\".\n\nВы можете использовать следующие комманды:\n/tasks - вопросы и задачи,\n/help - помощь,\n/reference - справка.".format(message.from_user))

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "/reference":
        bot.send_message(message.chat.id, "Я бот, который предлагает различные задачки и вопросы для улучшения изучения темы \"Информационная безопасность\".")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Используй активные кнопки внизу для получения необходимой информации.")
    elif message.text == "/tasks":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите подходящий тип вопросов для проверки знаний", reply_markup=on)
    elif message.text == "Ситуативные задачи":
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Ситуация 1', callback_data='situation1')
        key_second = types.InlineKeyboardButton(text='Ситуация 2', callback_data='situation2')
        key_third = types.InlineKeyboardButton(text='Ситуация 3', callback_data='situation3')
        key_fourth = types.InlineKeyboardButton(text='Ситуация 4', callback_data='situation4')
        keyboard.add(key_first,key_second,key_third,key_fourth)
        bot.send_message(message.chat.id,"Выберите ситуацию, которую хотите рассмотреть", reply_markup=keyboard)
    elif message.text == "Да/Нет":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        exit = types.KeyboardButton("Выход🚪")
        on.add(exit)
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Да', callback_data='Yes')
        key_second = types.InlineKeyboardButton(text='Нет', callback_data='No')
        keyboard.add(key_first, key_second)
        bot.send_message(message.chat.id, "На следующие вопросы по теме \"Информационная безопасность\" отвечайте Да/Нет, для того, чтобы проверить свои знания.", reply_markup=on)
        bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)
    elif message.text == "Назад ↩":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Ситуация 1', callback_data='situation1')
        key_second = types.InlineKeyboardButton(text='Ситуация 2', callback_data='situation2')
        key_third = types.InlineKeyboardButton(text='Ситуация 3', callback_data='situation3')
        key_fourth = types.InlineKeyboardButton(text='Ситуация 4', callback_data='situation4')
        keyboard.add(key_first, key_second, key_third, key_fourth)
        bot.send_message(message.chat.id, "Вы вернулись назад",reply_markup=on)
        bot.send_message(message.chat.id, "Выберите ситуацию, которую хотите рассмотреть", reply_markup=keyboard)
    elif message.text == "Выход🚪":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Вы вышли назад", reply_markup=on)
        bot.send_message(message.chat.id, "Выберите подходящий тип вопросов для проверки знаний")
    elif message.text == "Тест":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.KeyboardButton("Старт▶")
        exit = types.KeyboardButton("Выход🚪")
        on.add(start, exit)
        bot.send_message(message.chat.id, "Пройдите тест по теме \"Информационная безопасность\", чтобы удостовериться в том, что Вы сможете обеспечить безопасность себе и Вашим устройствам.", reply_markup=on)
    else:
        situations(message)

def test(message):
    if message.text == "Старт▶":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Всегда")
        b2 = types.KeyboardButton("Знаете отправителя")
        b3 = types.KeyboardButton("Никогда")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "В каких случаях Вы можете быть уверены в том, что электронное письмо будет получено от указанного отправителя?", reply_markup=on)
    elif message.text == "Всегда":
        bot.send_message(message.chat.id, "Неправильно!\nПопробуйте еще!")
    elif message.text == "Никогда":
        bot.send_message(message.chat.id, "Неправильно!\nПодумайте еще!")
    elif message.text == "Знаете отправителя":
        bot.send_message(message.chat.id, "Верно!\nСледующий вопрос:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Открыть его")
        b2 = types.KeyboardButton("Открыть вложение")
        b3 = types.KeyboardButton("Удалить, не открывая")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Что нужно сделать при получении подозрительного сообщения электронной почты?", reply_markup=on)
    elif message.text == "Открыть его":
        bot.send_message(message.chat.id, "Нет, так делать не стоит, это может быть вирус.\nПопробуйте еще!")
    elif message.text == "Открыть вложение":
        bot.send_message(message.chat.id, "Нет, так делать не стоит, это может быть вирус.\nПодумайте еще!")
    elif message.text == "Удалить, не открывая":
        bot.send_message(message.chat.id, "Верно!\nПереходим к следующему вопросу:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Удалить/Фильтр")
        b2 = types.KeyboardButton("Открыть")
        b3 = types.KeyboardButton("Ответить")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Какие меры следует предпринять при получении большого количества спама?", reply_markup=on)
    elif message.text == "Удалить/Фильтр":
        bot.send_message(message.chat.id, "Молодец!\nСледующее задание:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Хранить на жестком диске")
        b2 = types.KeyboardButton("Отправить другу")
        b3 = types.KeyboardButton("Резервные копии файлов")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Что следует делать с важными файлами?", reply_markup=on)
    elif message.text == "Открыть":
        bot.send_message(message.chat.id, "Могут возникнуть проблемы, если Вы так поступите.\nПодумайте еще!")
    elif message.text == "Ответить":
        bot.send_message(message.chat.id, "Могут возникнуть проблемы, если Вы так поступите.\nПопробуйте еще!")
    elif message.text == "Хранить на жестком диске":
        bot.send_message(message.chat.id, "Это неверный ответ! Так небезопасно.\nПодумайте еще!")
    elif message.text == "Отправить другу":
        bot.send_message(message.chat.id, "Это неверный ответ! Так небезопасно.\nПопробуйте еще!")
    elif message.text == "Резервные копии файлов":
        bot.send_message(message.chat.id, "Правильно!\nПереходим к следующему вопросу:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Нет")
        b2 = types.KeyboardButton("Да")
        b3 = types.KeyboardButton("При открытии доступа")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Можно ли проникнуть в незащищенный компьютер другого пользователя с другого компьютера?", reply_markup=on)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, "Неправильно!\nПопробуйте еще!")
    elif message.text == "Да":
        bot.send_message(message.chat.id, "Это верный ответ!\nСледующий вопрос звучит так:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Хобби")
        b2 = types.KeyboardButton("Псевдоним")
        b3 = types.KeyboardButton("Номер телефона")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Какую информацию не следует разглашать в чатах и дискуссионных группах?", reply_markup=on)
    elif message.text == "При открытии доступа":
        bot.send_message(message.chat.id, "Неправильно!\nПодумайте еще!")
    elif message.text == "Хобби":
        bot.send_message(message.chat.id, "Нет, это неверный ответ! Вы можете разглашать информацию о Вашем хобби, при желании.\nПодумайте еще!")
    elif message.text == "Номер телефона":
        bot.send_message(message.chat.id, "Молодец!\nСледующее задание:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Антивирусные программы")
        b2 = types.KeyboardButton("Компьютерная служба помощи")
        b3 = types.KeyboardButton("Закрытие браузера")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Какие меры необходимо принять, чтобы нежелательные посетители не могли проникнуть в Ваш компьютер через Интернет?", reply_markup=on)
    elif message.text == "Псевдоним":
        bot.send_message(message.chat.id, "Нет, это неверно!Вы можете разглашать свой псевдоним, так как он не распространяет Вашу личную информацию.\nПопробуйте еще!")
    elif message.text == "Закрытие браузера":
        bot.send_message(message.chat.id, "Нет, так нельзя достичь необходимого результата.\nПодумайте еще!")
    elif message.text == "Антивирусные программы":
        bot.send_message(message.chat.id, "Верно!\nПереходим к следующему вопросу:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Только преступники")
        b2 = types.KeyboardButton("Клавиатура")
        b3 = types.KeyboardButton("Просмотр веб-страниц")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Как могут распространяться компьютерные вирусы?", reply_markup=on)
    elif message.text == "Компьютерная служба помощи":
        bot.send_message(message.chat.id, "Нет, так нельзя достичь необходимого результата.\nПопробуйте еще!")
    elif message.text == "Только преступники":
        bot.send_message(message.chat.id, "Не только преступники распространяют компьютерные вирусы.\nПодумайте еще!")
    elif message.text == "Просмотр веб-страниц":
        bot.send_message(message.chat.id, "Да, это так.\nСледующий вопрос:")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Sneghinka")
        b2 = types.KeyboardButton("Ekaterina")
        b3 = types.KeyboardButton("KIvanova")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Какой из предложенных NIK-ов предпочтительней выбрать Ивановой Екатерине для обеспечения безопасного общения на веб-узле?", reply_markup=on)
    elif message.text == "Клавиатура":
        bot.send_message(message.chat.id, "При помощи клавиатуры не могут распространяться компьютерные вирусы.\nПодумайте еще!")
    elif message.text == "Sneghinka":
        bot.send_message(message.chat.id, "Это хороший NIK, чтобы не разглашать в сети Интернет свою личную ифнормацию.\nПереходим к следующему заданию::")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Поставщик услуг")
        b2 = types.KeyboardButton("Создатели")
        b3 = types.KeyboardButton("Никто")
        b4 = types.KeyboardButton("Выход🚪")
        on.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Кто несет ответственность за материал, который публикуется в Интернете?", reply_markup=on)
    elif message.text == "Ekaterina":
        bot.send_message(message.chat.id, "Это неудачный вариант, так как разглашает имя пользователя.\nПопробуйте еще!")
    elif message.text == "KIvanova":
        bot.send_message(message.chat.id, "Это неудачный вариант, так как разглашает имя и фамилию пользователя.\nПодумайте еще!")
    elif message.text == "Поставщик услуг":
        bot.send_message(message.chat.id, "Нет, это не так. Поставщик услуг не несет ответственность.\nПопробуйте еще!")
    elif message.text == "Создатели":
        bot.send_message(message.chat.id, "Да, создатели несут ответственность за материал, который публикуется в Интернете.")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Поздравляю, тест окончен. Основываясь на результатах, Вы получили дополнительную информацию и сейчас прекрасно понимаете, как обезопасить себя и Ваши устройства.", reply_markup=on)
    elif message.text == "Никто":
        bot.send_message(message.chat.id, "Нет, это не так.\nПодумайте еще!")
    else:
        bot.send_message(message.chat.id, "{0.first_name}, я помощник, предназначенный для обучения по теме \"Информационная безопасность\".\n\nВы можете использовать следующие комманды:\n/tasks - вопросы и задачи,\n/help - помощь,\n/reference - справка.".format(message.from_user))

def situations(message):
    if message.text == "1️⃣1️⃣":
        bot.send_message(message.chat.id, "Не стоит проявлять свою агрессию на незнакомого Вам человека.\nПодумайте еще!")
    elif message.text == "1️⃣2️⃣":
        bot.send_message(message.chat.id, "Ни в коем случае нельзя так поступать, так как могут возникнуть негативные последствия как для вас, так и для вашего устройства.\nПодумайте еще!")
    elif message.text == "1️⃣3️⃣":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key1, key2)
        bot.send_message(message.chat.id, "Возможно и такое решение ситуации, но стоит все-таки быть отсорожным, Вы не знаете, что это за человек.\nХотите продолжить?",reply_markup=keyboard)
    elif message.text == "1️⃣4️⃣":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key1, key2)
        bot.send_message(message.chat.id, "Верно, скорее всего, это лучший способ, чтобы сохранить Ваши данные и устройство от нежелательных последствий.\nХотите продолжить?",reply_markup=keyboard)
    elif message.text == "2️⃣1️⃣":
        bot.send_message(message.chat.id, "Ни в коем случае нельзя так поступать, так как могут возникнуть негативные последствия как для вас, так и для вашего устройства.\nПодумайте еще!")
    elif message.text == "2️⃣2️⃣":
        bot.send_message(message.chat.id, "Возможно и такое решение ситуации, но лучше не вводить личные данные и не получать различную информацию из непроверенных источников.\nПодумайте еще!")
    elif message.text == "2️⃣3️⃣":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key1, key2)
        bot.send_message(message.chat.id, "Верно, скорее всего, это лучший способ, чтобы сохранить Ваши данные и устройство от нежелательных последствий.\nХотите продолжить?",reply_markup=keyboard)
    elif message.text == "2️⃣4️⃣":
        bot.send_message(message.chat.id, "Конечно можно поступить так, но лучше не стоит, так как можно ошибиться.\nПодумайте еще!")
    elif message.text == "3️⃣1️⃣":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key1, key2)
        bot.send_message(message.chat.id, "Верно, скорее всего, это лучший способ, чтобы не поддаться влиянию мошенников. Если хотите помочь больным детям, всегда проверяйте источники информации.\nХотите продолжить?",reply_markup=keyboard)
    elif message.text == "3️⃣2️⃣":
        bot.send_message(message.chat.id, "Не стоит сбрасывать звонок от Вашего друга. Вы поступите некрасиво по отношению к нему.\nПодумайте еще!")
    elif message.text == "3️⃣3️⃣":
        bot.send_message(message.chat.id, "Не лучшее решение, так как это Ваш друг и это обязательно его обидит.\nПодумайте еще!")
    elif message.text == "3️⃣4️⃣":
        bot.send_message(message.chat.id, "Нет, такое решение ситуации будет неверным, так как данные сообщения в Интернете часто оказываются мошенниками и средства, переведенные Вами, пойдут совсем не на помощь больным детям. Обращайтесь в проверенные источники, если хотите помочь.\nПодумайте еще!")
    elif message.text == "4️⃣1️⃣":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key1, key2)
        bot.send_message(message.chat.id, "Да, можно поступить так, не обязательно отвечать незнакомым людям.\nХотите продолжить?", reply_markup=keyboard)
    elif message.text == "4️⃣2️⃣":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key1, key2)
        bot.send_message(message.chat.id, "Хороший вариант, следует удостовериться в том, что отправитель не врет, тогда можно познакомиться поближе.\nХотите продолжить?", reply_markup=keyboard)
    elif message.text == "4️⃣3️⃣":
        bot.send_message(message.chat.id, "Не стоит так делать. Если это незнакомый Вам человек, то не соглашайтесь на личную встречу, так как могут возникнуть неприятности.\nПодумайте еще!")
    elif message.text == "4️⃣4️⃣":
        bot.send_message(message.chat.id, "Не стоит проявлять свою агрессию на незнакомого Вам человека.\nПодумайте еще!")
    else:
        test(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "situation1":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1️⃣1️⃣")
        button2 = types.KeyboardButton("1️⃣2️⃣")
        button3 = types.KeyboardButton("1️⃣3️⃣")
        button4 = types.KeyboardButton("1️⃣4️⃣")
        button5 = types.KeyboardButton("Назад ↩")
        on.add(button1, button2, button3, button4,button5)
        bot.send_message(call.message.chat.id, text="Вы общаетесь в социальной сети со своими друзьями. Неожиданно от незнакомого человека приходит сообщение: «Привет, у тебя отличные фото! Только у меня все равно круче! Жми скорее сюда!». Предлагается перейти по ссылке для просмотра фотографий. Как следует поступить в данной ситуации?")
        bot.send_message(call.message.chat.id,text="Варианты ответа:\n1.1. Агрессивно повести себя по отношению к незнакомцу.\n1.2. Конечно перейти по ссылке и посмотреть фотографии, может они и в правду круче.\n1.3. Не переходить по ссылке, но завести разговор с этим человеком. Вдруг он Вас знает лично.\n1.4. Никак не взаимодействовать с данным сообщением.",reply_markup=on)
    elif call.data == "situation2":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("2️⃣1️⃣")
        button2 = types.KeyboardButton("2️⃣2️⃣")
        button3 = types.KeyboardButton("2️⃣3️⃣")
        button4 = types.KeyboardButton("2️⃣4️⃣")
        button5 = types.KeyboardButton("Назад ↩")
        on.add(button1, button2, button3, button4, button5)
        bot.send_message(call.message.chat.id, text="Вы находитесь в сети Интернет, изучаете сайты с информацией о далеких планетах. Вдруг наталкиваетесь на сайт, который предлагает составить Ваш личный гороскоп. Вы переходите по ссылке, отвечаете на все предложенные вопросы. В конце опроса Вам предлагается ввести номер мобильного телефона. Какими будут Ваши действия?")
        bot.send_message(call.message.chat.id, text="Варианты ответа:\n2.1. Следует ввести свой номер телефона, чтобы получить личный гороскоп.\n2.2. Не вводить свой номер телефона и попробовать получить личный гороскоп без учета этих данных.\n2.3. Вернуться назад, не отправляя личные данные.\n2.4. Отправить жалобу и заблокировать программное средство для составление Вашего личного гороскопа.", reply_markup=on)
    elif call.data == "situation3":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("3️⃣1️⃣")
        button2 = types.KeyboardButton("3️⃣2️⃣")
        button3 = types.KeyboardButton("3️⃣3️⃣")
        button4 = types.KeyboardButton("3️⃣4️⃣")
        button5 = types.KeyboardButton("Назад ↩")
        on.add(button1, button2, button3, button4, button5)
        bot.send_message(call.message.chat.id, text="Вам позвонил друг и сообщил, что увидел в Интернет сообщение о срочном сборе средств для больного ребенка. Деньги предлагается перевести на счет указанного мобильного телефона или на электронный кошелек. Ваш друг настаивает на помощи ребенку. Какими будут Ваши действия?")
        bot.send_message(call.message.chat.id,text="Варианты ответа:\n3.1. Не скидывать деньги и попробовать переубедить друга.\n3.2. Ответить отрицательно и сбросить звонок.\n3.3. Агрессивно себя повести по отношению к другу.\n3.4. Проявить помощь и скинуть с другом средства для больного ребенка.", reply_markup=on)
    elif call.data == "situation4":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("4️⃣1️⃣")
        button2 = types.KeyboardButton("4️⃣2️⃣")
        button3 = types.KeyboardButton("4️⃣3️⃣")
        button4 = types.KeyboardButton("4️⃣4️⃣")
        button5 = types.KeyboardButton("Назад ↩")
        on.add(button1, button2, button3, button4, button5)
        bot.send_message(call.message.chat.id, text="Во время общения в социальной сети Вам приходит сообщение: «Привет! Мы с тобой как-то виделись у наших общих друзей. Решил тебя найти в сетях. Классная у тебя страничка! Может пойдем вечером гулять?» Как Вы поступите в этой ситуации?")
        bot.send_message(call.message.chat.id,text="Варианты ответа:\n4.1. Проигнорировать данное сообщение.\n4.2. Ответить на данное сообщение, но попробовать узнать больше про человека и Ваших общих друзей.\n4.3. Согласиться встретиься, так как у вас есть общие знакомые.\n4.4. Проявить враждебное отношение к отправителю.", reply_markup=on)
    elif call.data == "yes":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Ситуация 1', callback_data='situation1')
        key_second = types.InlineKeyboardButton(text='Ситуация 2', callback_data='situation2')
        key_third = types.InlineKeyboardButton(text='Ситуация 3', callback_data='situation3')
        key_fourth = types.InlineKeyboardButton(text='Ситуация 4', callback_data='situation4')
        keyboard.add(key_first, key_second, key_third, key_fourth)
        bot.send_message(call.message.chat.id,"Можете продолжить",reply_markup=on)
        bot.send_message(call.message.chat.id, "Выберите ситуацию, которую хотите рассмотреть", reply_markup=keyboard)
    elif call.data == "no":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(call.message.chat.id, "Выберите подходящий тип вопросов для проверки знаний", reply_markup=on)
    elif call.data == "Yes":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y1')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n1')
        keyboard.add(key1,key2)
        bot.send_message(call.message.chat.id, "Могут ли вредоносные программы украсть Вашу переписку с друзьями?", reply_markup=keyboard)
    elif call.data == "No":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(call.message.chat.id, "Ладно, попробуйте позже", reply_markup=on)
    elif call.data == "y1":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y2')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n2')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Можно ли скачивать игры с неизвестных сайтов?", reply_markup=keyboard)
    elif call.data == "n1":
        bot.send_message(call.message.chat.id, "Неправильный ответ. Вредоносные программы могут украсть Вашу переписку с друзьями, поэтому будьте аккуратны.")
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y2')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n2')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Можно ли скачивать игры с неизвестных сайтов?", reply_markup=keyboard)
    elif call.data == "y2":
        bot.send_message(call.message.chat.id, "Неверно, не стоит рисковать и скачивать игры с незнакомых сайтов, ведь под игрой может быть вирус. который нанесет вред Вашим данным.")
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y3')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n3')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Можно ли открывать письма от неизвестного Вам человека, если он предлагает перейти по определенной ссылке, чтобы посмотреть фотографии, картинки?", reply_markup=keyboard)
    elif call.data == "n2":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y3')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n3')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Можно ли открывать письма от неизвестного Вам человека, если он предлагает перейти по определенной ссылке, чтобы посмотреть фотографии, картинки?", reply_markup=keyboard)
    elif call.data == "y3":
        bot.send_message(call.message.chat.id, "Это неверный выбор. Ни в коем случае нельзя открывать такие письма, ведь при помощи таких ссылок могут быть украдены Ваши личные данные, либо установлены вирусы на устройство.")
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y4')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n4')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Может ли общение в социальных сетях принести вам какой-нибудь вред?", reply_markup=keyboard)
    elif call.data == "n3":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y4')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n4')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Может ли общение в социальных сетях принести вам какой-нибудь вред?", reply_markup=keyboard)
    elif call.data == "y4":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y5')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n5')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Можно ли использовать сеть Интернет безо всяких опасений?", reply_markup=keyboard)
    elif call.data == "n4":
        bot.send_message(call.message.chat.id, "Неправильно, конечно может, поэтому стоит ответственно подходить к общению в социальных сетях, особенно с незнакомыми людьми.")
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y5')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n5')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Можно ли использовать сеть Интернет безо всяких опасений?", reply_markup=keyboard)
    elif call.data == "y5":
        bot.send_message(call.message.chat.id, "Неверно, стоит думать и следить за своими действиями в сети Интернет, так как можно получить неприятные последствия.")
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y6')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n6')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Все ли сайты в интернете безопасны?", reply_markup=keyboard)
    elif call.data == "n5":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='y6')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='n6')
        keyboard.add(key1, key2)
        bot.send_message(call.message.chat.id, "Все ли сайты в интернете безопасны?", reply_markup=keyboard)
    elif call.data == "y6":
        bot.send_message(call.message.chat.id, "Это неправильно. Большинство сайтов в сети Интернет небезопасны, поэтому будьте осторожны перед тем, как переходить по различным ссылкам.")
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(call.message.chat.id, "Поздравляю, Вы ответили на все вопросы. Основываясь на результатах, Вы получили дополнительную информацию по теме \"Информационная безопасность\", что предотвратит появление неприятных ситуаций.", reply_markup=on)
    elif call.data == "n6":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ситуативные задачи")
        button2 = types.KeyboardButton("Да/Нет")
        button3 = types.KeyboardButton("Тест")
        on.add(button1, button2, button3)
        bot.send_message(call.message.chat.id, "Поздравляю, Вы ответили на все вопросы. Основываясь на результатах, Вы получили дополнительную информацию по теме \"Информационная безопасность\", что предотвратит появление неприятных ситуаций.", reply_markup=on)

bot.polling(none_stop=True, interval=0)