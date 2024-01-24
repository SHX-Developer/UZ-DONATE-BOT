from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

import sqlite3
import datetime

import config
import data
import inline_markups
import display



#  Library Variables

bot = Bot(config.token)
dp = Dispatcher(bot)

db = sqlite3.connect('database.db', check_same_thread = False)
sql = db.cursor()

date_time = datetime.datetime.now().date()






#  Add new user data to database
async def add_new_user(message):
    sql.execute('INSERT INTO user_access (id, username, firstname, lastname, date) VALUES (?, ?, ?, ?, ?)',
    (message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, date_time))
    sql.execute('INSERT INTO user_data (id, language, currency, reg_status) VALUES (?, ?, ?, ?)',
    (message.chat.id, '-', '-', 'no'))
    db.commit()




#  Request Currency
async def request_currency(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        request_currency_text = data.uz_register_currency_text
    else:
        request_currency_text = data.ru_register_currency_text

    await bot.send_message(
        chat_id = call.message.chat.id,
        text = request_currency_text,
        parse_mode = 'html',
        reply_markup = inline_markups.register_currency)
    

    






#  Send greeting
async def send_greeting(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        greeting = data.uz_greeting_text
    else:
        greeting = data.ru_greeting_text

    await bot.send_message(
        chat_id = call.message.chat.id, 
        text = greeting,
        parse_mode = 'html')

    


#  Send menu (MESSAGE)
async def send_menu_message(message):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        menu = inline_markups.uz_menu
    else:
        menu = inline_markups.ru_menu
    
    with open('photo/channel_photo.jpg', 'rb') as photo:
        await bot.send_photo(
            chat_id = message.chat.id,
            photo = photo,
            parse_mode = 'html',
            reply_markup = menu)
    

    
        
#  Send menu (CALL)
async def send_menu_call(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        menu = inline_markups.uz_menu
    else:
        menu = inline_markups.ru_menu
    
    with open('photo/channel_photo.jpg', 'rb') as photo:
        await bot.send_photo(
            chat_id = call.message.chat.id,
            photo = photo,
            parse_mode = 'html',
            reply_markup = menu)









#  Add UZS
async def add_uzs_currency(call):
    sql.execute('UPDATE user_data SET currency = ? WHERE id = ?', ('uzs', call.message.chat.id))
    db.commit()
    await display.display_currency(call)

#  Add RUB
async def add_rub_currency(call):
    sql.execute('UPDATE user_data SET currency = ? WHERE id = ?', ('rub', call.message.chat.id))
    db.commit()
    await display.display_currency(call)





#  Add Uzbek Language
async def add_uzbek_language(call):
    sql.execute('UPDATE user_data SET language = ? WHERE id = ?', ('uzbek', call.message.chat.id))
    db.commit()
    await display.display_language(call)

#  Add Russian Language
async def add_russian_language(call):
    sql.execute('UPDATE user_data SET language = ? WHERE id = ?', ('russian', call.message.chat.id))
    db.commit()
    await display.display_language(call)
    
