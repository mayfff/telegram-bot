import telebot
from telebot import types
ENABLE_MIDDLEWARE = True
SESSION_TIME_TO_LIVE = 5 * 60
bot = telebot.TeleBot('5826597344:AAEImoEslAM3jv1okyw6eIIHvBK2dw2Yuhc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привіт, <b>{message.from_user.first_name} </b> \n' \
        'Мої команди: /schedule , /books'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

@bot.message_handler(commands=['schedule'])
def schedule(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True ,row_width=1)
    itembtn1 = types.InlineKeyboardButton('Понеділок - лекції')
    itembtn2 = types.InlineKeyboardButton('Вівторок - лаби')
    itembtn3 = types.InlineKeyboardButton('Середа - лекції')
    itembtn4 = types.InlineKeyboardButton('Четвер - практика')
    itembtn5 = types.InlineKeyboardButton("П'ятниця")
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(message.chat.id, "Обери день:", reply_markup=markup)
    print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

@bot.message_handler(commands=['books'])
def books(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True ,row_width=3)
    itembtn1 = types.InlineKeyboardButton('Метода СДА')
    itembtn2 = types.InlineKeyboardButton('Конспект СДА')
    itembtn3 = types.InlineKeyboardButton('Метода Програмування')
    itembtn4 = types.InlineKeyboardButton('Конспект Програмування')
    itembtn5 = types.InlineKeyboardButton('Метода КЛ')
    itembtn6 = types.InlineKeyboardButton('Конспект ЛААГ')    
    itembtn7 = types.InlineKeyboardButton('Метода курсач КЛ')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    bot.send_message(message.chat.id, "Обери підручник:", reply_markup=markup)
    print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

@bot.message_handler()
def get_user_text(message):
    if(message.text == 'Метода СДА'):
        file = open(r'D:/КПІ/Методи/сда метода 1.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        file = open(r'D:/КПІ/Методи/сда метода 2.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

    elif(message.text == 'Конспект СДА'):
        file = open(r'D:/КПІ/Методи/сда конспект.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

    elif(message.text == 'Метода Програмування'):
        file = open(r'D:/КПІ/Методи/програмування метода.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')


    elif(message.text == 'Конспект Програмування'):
        file = open(r'D:/КПІ/Методи/програмування конспект.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')
        
        
    elif(message.text == 'Метода КЛ'):
        file = open(r'D:/КПІ/Методи/кл метода.docx', 'rb')
        bot.send_document(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')
        
        
    elif(message.text == 'Конспект ЛААГ'):
        file = open(r'D:/КПІ/Методи/Конспект лекцій ЛААГ.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id -  {message.from_user.id}')


    elif(message.text == 'Метода курсач КЛ'):
        file = open(r'D:/КПІ/Методи/Метода курсач КЛ.pdf', 'rb')
        bot.send_document(message.chat.id, file);
        print(f'{message.text} by {message.from_user.first_name} id -  {message.from_user.id}')


    elif(message.text == 'Понеділок - лекції'):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        itembtn11 = types.InlineKeyboardButton('СДА', url='https://bbb.comsys.kpi.ua/b/ana-gca-2xm')
        itembtn21 = types.InlineKeyboardButton('Вишмат', url='https://us04web.zoom.us/j/79880807244?pwd=IOPT7X4Y5ltrQEtfjMoLVF0EXLEed2.1')
        itembtn31 = types.InlineKeyboardButton('ОЗСЖ', url='https://us02web.zoom.us/j/4387354937?pwd=R3R3NkpWU09GY3kvanZBeEcrQWZoUT09')
        itembtn41 = types.InlineKeyboardButton('Програмування', url='https://us02web.zoom.us/j/5060383482?pwd=Qk9HZGtIdVdFVHNFd0ZCY1lJbitvdz09')
        markup1.add(itembtn11, itembtn21, itembtn31, itembtn41)
        bot.send_message(message.chat.id, "Тиждень 1/2\nПари 1-4 (8:30 - 15:50)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        itembtn12 = types.InlineKeyboardButton('СДА', url='https://bbb.comsys.kpi.ua/b/ana-gca-2xm')
        itembtn22 = types.InlineKeyboardButton('Вишмат', url='https://us04web.zoom.us/j/79880807244?pwd=IOPT7X4Y5ltrQEtfjMoLVF0EXLEed2.1')
        itembtn32 = types.InlineKeyboardButton('Вишмат', url='https://us04web.zoom.us/j/79880807244?pwd=IOPT7X4Y5ltrQEtfjMoLVF0EXLEed2.1')
        itembtn42 = types.InlineKeyboardButton('Програмування', url='https://us02web.zoom.us/j/5060383482?pwd=Qk9HZGtIdVdFVHNFd0ZCY1lJbitvdz09')
        markup2.add(itembtn12, itembtn22, itembtn32, itembtn42)
        bot.send_message(message.chat.id, "Тиждень 2/2\nПари 1-4 (8:30 - 15:50)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup2)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')


    elif(message.text == 'Вівторок - лаби'):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        itembtn11 = types.InlineKeyboardButton("КЛ", url='https://us04web.zoom.us/j/7382214783?pwd=RnZ3SWgwK1JoVkZtNndnKzdPZjFGdz09')
        itembtn21 = types.InlineKeyboardButton('Програмування', url='https://us05web.zoom.us/j/7089075754?pwd=TWRlZmxyVlFiTWU1UGlVVU1XcFE0Zz09')
        markup1.add(itembtn11, itembtn21)
        bot.send_message(message.chat.id, "Тиждень 1/2\nПари 3-4 (12:20 - 15:50)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        itembtn12 = types.InlineKeyboardButton('Перенесений вишмат', url='https://us02web.zoom.us/j/82183258793?pwd=TkZLeU1MY2d5eUpqeTJ5WUJTRHlVUT09')
        itembtn22 = types.InlineKeyboardButton('Програмування', url='https://us05web.zoom.us/j/7089075754?pwd=TWRlZmxyVlFiTWU1UGlVVU1XcFE0Zz09')
        markup2.add(itembtn12, itembtn22)
        bot.send_message(message.chat.id, "Тиждень 2/2\nПара 3-4 (12:20 - 15:50)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup2)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')


    elif(message.text == 'Середа - лекції'):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        itembtn11 = types.InlineKeyboardButton('ЛААГ', url='https://us02web.zoom.us/j/84756998362?pwd=cXJUZU10dU56U1V2QkFsZ01raG0vQT09')
        itembtn21 = types.InlineKeyboardButton('Програмування', url='https://us02web.zoom.us/j/5060383482?pwd=Qk9HZGtIdVdFVHNFd0ZCY1lJbitvdz09')
        itembtn31 = types.InlineKeyboardButton('КЛ', url='https://bbb.comsys.kpi.ua/b/val-zdp-vw0-dbr')
        markup1.add(itembtn11, itembtn21, itembtn31)
        bot.send_message(message.chat.id, "Однаковий на обидва тижні\nПари 2-4 (10:25 - 15:50)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup1)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')


    elif(message.text == 'Четвер - практика'):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        itembtn11 = types.InlineKeyboardButton('ЛААГ', url='https://us02web.zoom.us/j/89645375415?pwd=cXpFbXJNMk9ObWpsYXdobjdTeDViZz09')
        itembtn21 = types.InlineKeyboardButton('Вишмат', url='https://us02web.zoom.us/j/82183258793?pwd=TkZLeU1MY2d5eUpqeTJ5WUJTRHlVUT09')
        itembtn31 = types.InlineKeyboardButton('Англ', url='https://meet.google.com/bwg-pdnr-evh')
        itembtn41 = types.InlineKeyboardButton('Історія - лекція', url='https://meet.google.com/mif-wfzd-zqk')
        markup1.add(itembtn11, itembtn21, itembtn31, itembtn41)
        bot.send_message(message.chat.id, "Тиждень 1/2\nПари 1-4 (8:30 - 15:50)\nРозклад(натисни щоб під'єднатись):\nP.S: НА ІСТОРІЮ КРАЩЕ ЗАХОДИТИ ЧЕРЕЗ ГУГЛ КЛАС", reply_markup=markup1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        itembtn12 = types.InlineKeyboardButton('Вишмат', url='https://us02web.zoom.us/j/82183258793?pwd=TkZLeU1MY2d5eUpqeTJ5WUJTRHlVUT09')
        itembtn22 = types.InlineKeyboardButton('Англ', url='https://meet.google.com/bwg-pdnr-evh')
        markup2.add(itembtn12, itembtn22)
        bot.send_message(message.chat.id, "Тиждень 2/2\nПари 2-3 (10:25 - 13:55)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup2)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')


    elif(message.text == "П'ятниця"):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        itembtn11 = types.InlineKeyboardButton('Історія - СЕМІНАР!!', url='https://meet.google.com/mif-wfzd-zqk')
        itembtn21 = types.InlineKeyboardButton('Сда - лаби', url='https://us02web.zoom.us/j/88932218187?pwd=MUpFNjE3bHAxeEZ0NDE3NU0vYUUxZz09')
        markup1.add(itembtn11, itembtn21)
        bot.send_message(message.chat.id, "Тиждень 1/2\nПари1-2 (8:30 - 12:00)\nРозклад(натисни щоб під'єднатись):\nP.S: НА ІСТОРІЮ КРАЩЕ ЗАХОДИТИ ЧЕРЕЗ ГУГЛ КЛАС", reply_markup=markup1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        itembtn12 = types.InlineKeyboardButton('ОЗСЖ - практика', url='https://us05web.zoom.us/j/2035574145?pwd=bk1wTVhGbjJsQTR4WmVQMlROWFBCZz09')
        markup2.add(itembtn12)
        bot.send_message(message.chat.id, "Тиждень 2/2\nПара 2 (10:25 : 12:00)\nРозклад(натисни щоб під'єднатись):", reply_markup=markup2)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')
    

    elif(message.text.lower() == 'уба аба ня'):
        file = open(r'D:/ubauba.mp4', 'rb')
        bot.send_video(message.chat.id, file)
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

            
    else:
        mess = f'<b>Я тебе не розумію.</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        print(f'{message.text} by {message.from_user.first_name} id - {message.from_user.id}')

    bot.send_message(message.chat.id, '<b> Повернення в головне меню - /start </b>', parse_mode='html')

bot.infinity_polling()
