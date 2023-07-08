import telebot

token = ''

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message, word):
    if word in message:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)

# import telebot
#
# token = ''
#
# bot = telebot.TeleBot(token)
#
# my_name = 'Дима'
#
#
# @bot.message_handler(content_types=["text"])
# def echo(message):
#     if my_name in message.text:
#         text = 'Ба! Знакомые все лица'
#     else:
#         text = message.text
#     bot.send_message(message.chat.id, text)
#
#
# bot.polling(none_stop=True)
