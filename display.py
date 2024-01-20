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
    with open('photo/channel_photo.jpg', 'rb') as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.menu)



#  Display Games
async def display_games(call):
    with open('photo/channel_photo.jpg', 'rb') as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.games)
        




#  Display Mobile Legends Prices
async def display_mobile_legends(call):
    with open(f"photo/mobile_legends_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
                media = types.InputMedia(
                type = 'photo',
                media = photo,
                parse_mode = 'html',
                caption = data.mobile_legends_prices),
                chat_id = call.message.chat.id,
                message_id = call.message.message_id,
                reply_markup = inline_markups.mobile_legends)

#  Display Pubg
async def display_pubg(call):
    with open(f"photo/pubg_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = data.pubg_prices),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.pubg)

#  Display Free Fire
async def display_free_fire(call):
    with open(f"photo/free_fire_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = data.free_fire_prices),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.free_fire)

#  Display Clash Of Clans
async def display_clash_of_clans(call):
    with open(f"photo/clash_of_clans_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = data.clash_of_clans_prices),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.clash_of_clans)






#  Display Exchange
async def display_exchange(call):
    with open(f"photo/channel_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html',
            caption = data.exchange_info),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.exchange)



#  Display Currency
async def display_currency(call):
    with open(f"photo/channel_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html'),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.currency)



#  Display Language
async def display_language(call):
    with open(f"photo/channel_photo.jpg", "rb") as photo:
        await bot.edit_message_media(
            media = types.InputMedia(
            type = 'photo',
            media = photo,
            parse_mode = 'html'),
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = inline_markups.language)







