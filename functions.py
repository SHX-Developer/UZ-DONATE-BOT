from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

import sqlite3
import datetime

import config
import data
import inline_markups



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
    sql.execute('INSERT INTO user_data (id, language, currency) VALUES (?, ?, ?)',
    (message.chat.id, 'uzbek', 'uzs'))
    db.commit()



#  Send greeting
async def send_greeting(message):
    await bot.send_message(message.chat.id, data.greeting_text)

    

#  Send menu
async def send_menu(message):
    with open('photo/channel_photo.jpg', 'rb') as photo:
        await bot.send_photo(
            chat_id = message.chat.id,
            photo = photo,
            parse_mode = 'html',
            reply_markup = inline_markups.menu)
    await bot.send_message(message.chat.id, 'Выберите действие:')



