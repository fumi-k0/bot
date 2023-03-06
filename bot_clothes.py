from telebot import types
from telebot import TeleBot
from telebot.types import BotCommand

bot = TeleBot("5916345462:AAHGsAcKFrAec49hb3W8JcDp-bAONqgKPsc")

bot.set_my_commands([BotCommand('start', "Начать")])

markup_formality = types.InlineKeyboardMarkup()
markup_formality.add(types.InlineKeyboardButton("Формальная", callback_data='frml'))
markup_formality.add(types.InlineKeyboardButton("Неформальная", callback_data='unfrml'))

markup_merry = types.InlineKeyboardMarkup()
markup_merry.add(types.InlineKeyboardButton("Да", callback_data='merry_yes'))
markup_merry.add(types.InlineKeyboardButton("Нет", callback_data='no_merry'))

markup_work = types.InlineKeyboardMarkup()
markup_work.add(types.InlineKeyboardButton("Да", callback_data='work_yes'))
markup_work.add(types.InlineKeyboardButton("Нет", callback_data='work_no'))

luxury_style_women = """Вам подохдит шик стиль!\n\nДля женщин\n
Вам обязательно подойдёт красный комбинезон, сумочка  и утраченные босоножки , а так же добавим длинные серёжки для более дополненного образа.\n
"""

luxury_style_men = """Для мужчин\n 
Вам обязательно подойдёт приталленый костюм синего цвета, и не скучно, и отлично выделит вас! Так же можно добавить интересный галстук/бабочку и аксессуары."""

classic_style_women = """Женский стиль\n
Для вас отлично подойдёт классическая блуза с юбкой карандаш или брюками классических цветов (чёрный,  серый , синий) ,а так же образ дополнит классическмй жакет и утанченные туфли на каблуке.
"""

classic_style_men = """Мужской стиль\n

Для вас отлично подойдёт классический чёрный костюм с рубашкой, можно добавить галстук/бабочку. 
"""

casual_style_women = """Женщины\n 
Для вас подойдёт светлое романтичное платье с босоножками бежевого цвета , образ можно дополнить джинсовкой и крупной сумкой в цвет басаножек.
"""

casual_style_men = """Мужчины\n 
Вам подойдут светлые штаны и интересная рубашка  синих и голубых оттенков, образ можно дополнить интересным верхом, например пиджаком с геометрическими фигурами или одноцветным плащем.
"""

goodbye = "Надеюсь, я помог вам выбрать нужный стиль. До свидания!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="Добрый день!\n\nЯ помогу вам с выбором подходящей одежды. Скажите, пожалуйста, это формальная или неформальная встреча?", reply_markup=markup_formality)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "unfrml":
        bot.send_message(chat_id=call.message.chat.id, text="Эта часть пока в разработке, предлагаю рассмотреть формальный случай.")

    elif call.data == "frml":
        bot.send_message(chat_id=call.message.chat.id, text="Нужно выглядить празднично?", reply_markup=markup_merry)

    elif call.data == "merry_yes":
        bot.send_message(chat_id=call.message.chat.id, text=luxury_style_women)
        pic = open('lux_women.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=pic)
        pic.close()

        bot.send_message(chat_id=call.message.chat.id, text=luxury_style_men)
        pic = open('lux_men.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=pic)
        pic.close()

        bot.send_message(chat_id=call.message.chat.id, text=goodbye)

    elif call.data == "no_merry":
        bot.send_message(chat_id=call.message.chat.id, text="Встерча связана с работой?", reply_markup=markup_work)

    elif call.data == "work_yes":
        bot.send_message(chat_id=call.message.chat.id, text=classic_style_women)
        pic = open('women_classic.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=pic)
        pic.close()

        bot.send_message(chat_id=call.message.chat.id, text=classic_style_men)
        pic = open('men_classic.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=pic)
        pic.close()

        bot.send_message(chat_id=call.message.chat.id, text=goodbye)

    elif call.data == "work_no":

        bot.send_message(chat_id=call.message.chat.id, text=casual_style_women)
        pic = open('beige_woman.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=pic)
        pic.close()

        bot.send_message(chat_id=call.message.chat.id, text=casual_style_men)
        pic = open('man_casual.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=pic)
        pic.close()

        bot.send_message(chat_id=call.message.chat.id, text=goodbye)

bot.infinity_polling()
