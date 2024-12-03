import telebot
from telebot import types
import random
TOKEN='7723265534:AAFnfzyo4kyUXjFbVW8SxwEmtkj2CAWP4_g'

bot =telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Random')
    item2 = types.KeyboardButton('wallet')
    item3 = types.KeyboardButton('info')
    item4 = types.KeyboardButton('menu')

    markup.add(item1,item2,item3,item4)

    bot.send_message(message.chat.id,'Привет, {0.first_name}!'.format(message.from_user),reply_markup = markup)
    

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Random':
            bot.send_message(message.chat.id,'Ваше число:' + str(random.randint(0,1000)))
    elif message.text == 'wallet':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('dollar')
        item2 = types.KeyboardButton('evro')
        back=types.KeyboardButton('nazad')
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id,'wallet',reply_markup = markup)
    
    elif message.text == 'info':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('info _bot')
        item2 = types.KeyboardButton('chto_bot')
        back=types.KeyboardButton('nazad')
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id,'info',reply_markup = markup)
    
    elif message.text == 'menu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('nastroika')
        item2 = types.KeyboardButton('podpiska')
        item3 = types.KeyboardButton('mem')
        back=types.KeyboardButton('nazad')
        markup.add(item1, item2,item3, back)

        bot.send_message(message.chat.id,'menu',reply_markup = markup)

    elif message.text=='nazad':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Random')
        item2 = types.KeyboardButton('wallet')
        item3 = types.KeyboardButton('info')
        item4 = types.KeyboardButton('menu')

        markup.add(item1,item2,item3,item4)

        bot.send_message(message.chat.id,'nazad',reply_markup = markup)

bot.polling(none_stop = True)