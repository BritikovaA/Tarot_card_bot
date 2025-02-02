import telebot
import random
import datetime
from telebot import types


token = 'token'
bot = telebot.TeleBot(token)

def dayly_card(number):
    dict_card = {1: '<b> 🎪ДУРАК🎪 (прямое положение) </b> ...',
                 23: '<b> 🎪ДУРАК🎪 (перевернутое положение) </b> ...',
                 2: '<b> 💥МАГ💥 (прямое положение)</b> ...',
                 24: '<b> 💥МАГ💥 (перевернутое положение)</b> ...',
                 3: '<b> 🎎ВЕРХОВНАЯ ЖРИЦА🎎 (прямое положение)</b> ...',
                 25: '<b> 🎎ВЕРХОВНАЯ ЖРИЦА🎎 (перевернутое положение)</b> ...',
                 4: '<b> 👑ИМПЕРАТРИЦА👑 (прямое положение)</b> ...',
                 26: '<b> 👑ИМПЕРАТРИЦА👑 (перевернутое положение)</b> ...',
                 5: '<b> 👑ИМПЕРАТОР👑 (прямое положение)</b> ...',
                 27: '<b> 👑ИМПЕРАТОР👑 (перевернутое положение)</b> ...',
                 6: '<b> 🎎ЖРЕЦ🎎 (прямое положение)</b> ...',
                 28: '<b> 🎎ЖРЕЦ🎎 (перевернутое положение)</b> ...',
                 7: '<b> 💞ВЛЮБЛЕННЫЕ💞 (прямое положение)</b> ...',
                 29: '<b> 💞ВЛЮБЛЕННЫЕ💞(перевернутое положение)</b> ...',
                 8: '<b> 🐴КОЛЕСНИЦА🐴 (прямое положение)</b> ...',
                 30: '<b> 🐴КОЛЕСНИЦА 🐴(перевернутое положение)</b> ...',
                 9: '<b> 💪СИЛА💪 (прямое положение)</b> ...',
                 31: '<b> 💪СИЛА💪(перевернутое положение)</b> ...',
                 10: '<b> 🍃ОТШЕЛЬНИК🍃 (прямое положение)</b> ...',
                 32: '<b> 🍃ОТШЕЛЬНИК🍃 (перевернутое положение)</b> ...',
                 11: '<b> 🔮КОЛЕСО ФОРТУНЫ🔮 (прямое положение)</b> ...',
                 33: '<b💪> 🔮КОЛЕСО ФОРТУНЫ🔮 (перевернутое положение)</b> ...',
                 12: '<b> 💯СПРАВЕДЛИВОСТЬ💯 (прямое положение)</b> ...',
                 34: '<b> 💯СПРАВЕДЛИВОСТЬ💯 (перевернутое положение)</b> ...',
                 13: '<b> 🃏ПОВЕШЕННЫЙ🃏 (прямое положение)</b> ...',
                 35: '<b> 🃏ПОВЕШЕННЫЙ🃏 (перевернутое положение)</b> ...',
                 14: '<b> 🎃СМЕРТЬ🎃 (прямое положение)</b> ...',
                 36: '<b> 🎃СМЕРТЬ🎃 (перевернутое положение)</b> ...',
                 15: '<b> 🍚УМЕРЕННОСТЬ🍚 (прямое положение)</b> ...',
                 37: '<b> 🍚УМЕРЕННОСТЬ🍚 (перевернутое положение)</b> ...',
                 16: '<b> 😈ДЬЯВОЛ😈 (прямое положение)</b> ...',
                 38: '<b> 😈ДЬЯВОЛ😈 (перевернутое положение)</b> ...',
                 17: '<b> 🏯БАШНЯ🏯 (прямое положение)</b> ...',
                 39: '<b> 🏯БАШНЯ🏯 (перевернутое положение)</b> ...',
                 18: '<b> 🌠ЗВЕЗДА🌠 (прямое положение)</b> ...',
                 40: '<b> 🌠ЗВЕЗДА🌠 (перевернутое положение)</b> ...',
                 19: '<b> 🌜ЛУНА🌜 (прямое положение)</b> ...',
                 41: '<b> 🌜ЛУНА🌜 (перевернутое положение)</b> ...',
                 20: '<b> 🌞СОЛНЦЕ🌞 (прямое положение)</b> ...',
                 42: '<b> 🌞СОЛНЦЕ 🌞(перевернутое положение)</b> ...',
                 21: '<b> 🎓СУД🎓 (прямое положение)</b> ...',
                 43: '<b> 🎓СУД🎓 (перевернутое положение)</b> ...',
                 22: '<b> 🌍МИР🌍 (прямое положение)</b> ...',
                 44: '<b> 🌍МИР🌍 (перевернутое положение)</b>
    return(dict_card[number])


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поприветствовать еще раз 👋")
    btn2 = types.KeyboardButton("Карта дня 🃏")
    btn3 = types.KeyboardButton("Отправить фидбек 💬")
    btn4 = types.KeyboardButton("Какие обновления запланированы? 🌠")
    markup.add(btn1, btn2, btn3, btn4)
    name = message.from_user.first_name
    bot.send_message(message.chat.id, '✨Привет ' + str(name) + '!✨ \nЯ вижу, что ты хочешь приоткрыть завесу тайн и получить предсказание на затра? \nПопроси вытащить карту дня и я все расскажу тебе!💫', reply_markup=markup)



@bot.message_handler(func=lambda message: True)
def card_message(message):
    global last_message
    card = 'карт'
    day = 'дня'
    if last_message:
        file_path = 'feedback.txt'
        with open(file_path, 'a') as feedback_file:
            feedback_file.write(str(datetime.datetime.fromtimestamp(message.date)) + ' - ' + message.from_user.username + ' - ' + message.text + '\n')
        last_message = None
        bot.send_message(message.chat.id, text="Спасибо за ваш отзыв!✨")
    if(message.text == 'Поприветствовать еще раз 👋'):
        bot.send_message(message.chat.id, text=f'Здравствуй {message.from_user.first_name}!✨ \nХочешь посмотреть, что карты предвещают тебе сегодня?💫')
    if(message.text == 'Какие обновления запланированы? 🌠'):
        bot.send_message(message.chat.id, text='Конечно, основные планы - это добавление новых вариантов раскладов, улучшение трактовок, добавление изображений. Однако, мы всегда открыты к предложениям и с радостью учтем и возьмем на вооружение ваши идеи.⚡ \nНажимай кнопку "Фидбек", чтобы рассказать о них!🌙 ')
    if(message.text == 'Отправить фидбек 💬'):
        bot.send_message(message.chat.id, text='Спасибо большое, что решил уделить время и написать свой отзыв о боте или какие-либо предложения! Для нас это очень важно, ведь мы стараемся стать лучше.\n\n Сообщение, которое ты напишешь ниже, будет доставлено к нам и тщательно изучено. Спасибо 💖')
        last_message = message


    number = random.randint(1, 44)
    if card in message.text.lower() and day in message.text.lower():
        bot.send_message(message.chat.id, dayly_card(number), parse_mode='HTML')
        if number > 22:
            number -= 22
            image = Image.open(f'{number}.jpg')
            image_rotate = image.rotate(180, expand=True)
            bot.send_photo(message.chat.id, image_rotate)
        else:
            image = Image.open(f'{number}.jpg')
            bot.send_photo(message.chat.id, image)
        image.close()

bot.polling()
