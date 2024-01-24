from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

import sqlite3

import config
import data
import inline_markups



#  Library Variables

bot = Bot(config.token)
dp = Dispatcher(bot)

db = sqlite3.connect('database.db', check_same_thread = False)
sql = db.cursor()





#  Display Menu
async def display_menu(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        menu = inline_markups.uz_menu
    else:
        menu = inline_markups.ru_menu

    with open('photo/channel_photo.jpg', 'rb') as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = menu)



#  Display Games
async def display_games(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        games = inline_markups.uz_games
    else:
        games = inline_markups.ru_games

    with open('photo/games_photo.jpg', 'rb') as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = games)
        




#  Display Mobile Legends Prices
async def display_mobile_legends(call):
    user_currency = sql.execute(f'SELECT currency FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]

    if user_currency == 'uzs':
        price = data.uz_mobile_legends
    elif user_currency == 'rub':
        price = data.ru_mobile_legends
    
    if user_language == 'uzbek':
        mobile_legends = inline_markups.uz_mobile_legends
    else:
        mobile_legends = inline_markups.ru_mobile_legends

    with open(f"photo/mobile_legends_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = price),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = mobile_legends)


#  Display Pubg
async def display_pubg(call):
    user_currency = sql.execute(f'SELECT currency FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]

    if user_currency == 'uzs':
        price = data.uz_pubg
    elif user_currency == 'rub':
        price = data.ru_pubg
    
    if user_language == 'uzbek':
        pubg = inline_markups.uz_pubg
    else:
        pubg = inline_markups.ru_pubg

    with open(f"photo/pubg_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = price),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = pubg)


#  Display Free Fire
async def display_free_fire(call):
    user_currency = sql.execute(f'SELECT currency FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]

    if user_currency == 'uzs':
        price = data.uz_free_fire
    elif user_currency == 'rub':
        price = data.ru_free_fire
    
    if user_language == 'uzbek':
        free_fire = inline_markups.uz_free_fire
    else:
        free_fire = inline_markups.ru_free_fire

    with open(f"photo/free_fire_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = price),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = free_fire)


#  Display Clash Of Clans
async def display_clash_of_clans(call):
    user_currency = sql.execute(f'SELECT currency FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]

    if user_currency == 'uzs':
        price = data.uz_clash_of_clans
    elif user_currency == 'rub':
        price = data.ru_clash_of_clans
    
    if user_language == 'uzbek':
        clash_of_clans = inline_markups.uz_clash_of_clans
    else:
        clash_of_clans = inline_markups.ru_clash_of_clans

    with open(f"photo/clash_of_clans_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = price),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = clash_of_clans)




#  Contact
async def display_contact(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        contact = inline_markups.uz_contact
    else:
        contact = inline_markups.ru_contact

    with open(f"photo/contact_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html'),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = contact)








#  Display Exchange
async def display_exchange(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]
    if user_language == 'uzbek':
        exchange = inline_markups.uz_exchange
    else:
        exchange = inline_markups.ru_exchange

    with open(f"photo/exchange_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = data.exchange_info),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = exchange)











#  Display Currency
async def display_currency(call):
    user_currency = sql.execute(f'SELECT currency FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]

    #  UZ Currency
    uz_currency = InlineKeyboardMarkup()
    uz_currency.row(InlineKeyboardButton(text = "✅  UZS", callback_data = 'uzs'),
                    InlineKeyboardButton(text = "RUB", callback_data = "rub"))
    uz_currency.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))
    
    #  RU Currency
    ru_currency = InlineKeyboardMarkup()
    ru_currency.row(InlineKeyboardButton(text = "UZS", callback_data = 'uzs'),
                    InlineKeyboardButton(text = "✅  RUB", callback_data = "rub"))
    ru_currency.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))

    #  Check User Currency
    if user_currency == 'uzs':
        currency = uz_currency
    elif user_currency == 'rub':
        currency = ru_currency

    with open(f"photo/currency_photo.jpeg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html'),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = currency)







#  Display Language
async def display_language(call):
    user_language = sql.execute(f'SELECT language FROM user_data WHERE id = {call.message.chat.id}').fetchone()[0]

    uz_language = InlineKeyboardMarkup()
    uz_language.row(InlineKeyboardButton(text = "✅  O'zbekcha", callback_data = 'uzbek'),
                    InlineKeyboardButton(text = "Russcha", callback_data = "russian"))
    uz_language.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))

    ru_language = InlineKeyboardMarkup()
    ru_language.row(InlineKeyboardButton(text = "Узбекский", callback_data = 'uzbek'),
                    InlineKeyboardButton(text = "✅  Русский", callback_data = "russian"))
    ru_language.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))

    #  Check User Language
    if user_language == 'uzbek':
        language = uz_language
    elif user_language == 'russian':
        language = ru_language

    with open(f"photo/language_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html'),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = language)







