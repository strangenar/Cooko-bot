import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('/home/naki/TelegramBot/welcome.webp','rb')
    bot.send_sticker(message.chat.id, sti)
    
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    order = types.KeyboardButton("Order food")
    check = types.KeyboardButton("Check the menu")
    markup.add(order, check)
    bot.send_message(message.chat.id,"Welcome, {0.first_name}!\n ".format(message.from_user, bot.get_me()), 
    parse_mode='html', reply_markup = markup)
    
@bot.message_handler(content_types=['text'])
def echo(message):
    if message.chat.type == 'private':
        if message.text == 'Order food':
            bot.send_message(message.chat.id, 'No food')
        elif message.text == 'Check the menu':
            markup = types.InlineKeyboardMarkup(row_width = 2)
            genBut = types.InlineKeyboardButton("General menu", callback_data ='General')
            kidBut = types.InlineKeyboardButton("Kids menu", callback_data ='Kids')
            vegBut = types.InlineKeyboardButton("Vegetarian menu", callback_data ='Vegetarian')
            markup.add(genBut, kidBut, vegBut)
            bot.send_message(message.chat.id, 'Choose', reply_markup = markup)
        else:
            bot.send_message(message.chat.id, 'Bye')
@bot.callback_query_handler(func = lambda call: True) 
def callback_inline(call):
            try:
                if call.message:
                    if call.data == 'General':
                        bot.send_message(call.message.chat.id, 'Oops, it is not available yet')
                    elif call.data == 'Kids':
                        bot.send_message(call.message.chat.id, 'Oops, it is not available yet')
                    elif call.data == 'Vegetarian':
                        bot.send_message(call.message.chat.id, 'Oops, it is not available yet')
                               
                    #remove inline buttons
                    bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id,  
                    text="Check the menu", reply_markup = None)
                    #show alert
                    bot.answer_callback_query(chat_id = call.message.chat.id)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="text alert")
            except Exception as e:
                print(repr(e))
 
#RUN
bot.polling(none_stop=True)
