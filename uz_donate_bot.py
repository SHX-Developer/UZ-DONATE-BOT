from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
import datetime
import sqlite3

import config
import inline_markups
import reply_markups
import display
import data
import functions


#  Library Variables
storage = MemoryStorage()
bot = Bot(config.token)
dp = Dispatcher(bot, storage = MemoryStorage())

db = sqlite3.connect('database.db', check_same_thread = False)
sql = db.cursor()

date_time = datetime.datetime.now().date()



#  Class States
class States(StatesGroup):
    value = State()

#  Creating Databases
sql.execute('CREATE TABLE IF NOT EXISTS user_access (id INTEGER, username TEXT, firstname TEXT, lastname TEXT, date DATE)')
sql.execute('CREATE TABLE IF NOT EXISTS user_data (id INTEGER, language TEXT, currency TEXT)')
db.commit()








#  START COMMAND

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    user_id = sql.execute(f'SELECT id FROM user_access WHERE id = {message.chat.id}').fetchone()

    if user_id == None:
        await functions.add_new_user(message)
        await functions.send_greeting(message)
        await functions.send_menu(message)
    else:
        await functions.send_menu(message)




#  Message Handler
@dp.message_handler()
async def text(message: types.Message):
    pass




#  Callback Handler
@dp.callback_query_handler(lambda call: True)
async def callback_queries(call: types.CallbackQuery):


#  DONATE
    
    if call.data == 'donate':
        await display.display_games(call)
            

#  GAMES
            
    elif call.data == 'mobile_legends':
        await display.display_mobile_legends(call)
        

    elif call.data == 'pubg':
        await display.display_pubg(call)
    
    elif call.data == 'free_fire':
        await display.display_free_fire(call)
    
    elif call.data == 'clash_of_clans':
        await display.display_clash_of_clans(call)
            



#  EXCHANGE
    elif call.data == 'exchange':
        await display.display_exchange(call)



#  Contact
    elif call.data == 'contact':
        await display.display_contact(call)



#  Currency
    elif call.data == 'currency':
        await display.display_currency(call)

#  Language
    elif call.data == 'language':
        await display.display_language(call)


#  BACK

    #  Back Games
    elif call.data == 'back_games':
        await display.display_games(call)

    #  Back Menu
    elif call.data == 'back_menu':
        await display.display_menu(call)
        


#  CURRENCY
    
    #  UZS
    elif call.data == 'uzs':
        await functions.add_uzs_currency(call)

    #  RUB
    elif call.data == 'rub':
        await functions.add_rub_currency(call)



#  LANGUAGE
    
    #  Uzbek Language
    elif call.data == 'uzbek':
        await functions.add_uzbek_language(call)

    #  Russian Language
    elif call.data == 'russian':
        await functions.add_russian_language(call)











#  EDIT INLINE TEXT
    elif call.data == 'edit_inline':
        await bot.edit_message_text(
            chat_id = call.message.chat.id, 
            message_id = call.message.message_id, 
            text = '<b> TEXT </b>', 
            parse_mode = 'html', 
            reply_markup = None)


#  EDIT INLINE PHOTO
    if call.data == 'edit_photo':
        with open('photo/channel_photo.jpg', 'rb') as photo:
            bot.edit_message_media( 
                media = types.InputMedia(
                type = 'photo',
                media = photo,
                chat_id = call.message.chat.id,
                message_id = call.message.message_id,
                caption = data.exchange_info,
                parse_mode = 'html'),
                reply_markup = inline_markups.exchange)




#  STATES
@dp.message_handler(state = States.value)
async def check_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['value'] = message.text

        #  FINISH STATE
        if message.text == 'value':
            await state.finish()
        
        #  SET STATE
        if message.text == 'value':
            await States.value.set()
        
        #  NEXT STATE
        if message.text == 'value':
            await States.next()
        







#  DELETE MESSAGE 1
async def delete_message_1(message):
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
    except:
        pass

#  DELETE MESSAGE 2
async def delete_message_2(message):
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 1)
    except:
        pass

#  DELETE MESSAGE 3
async def delete_message_3(message):
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 1)
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 2)
    except:
        pass

#  DELETE MESSAGE 1
async def delete_call_message_1(call):
    try:
        await bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id + 1)
    except:
        pass

#  DELETE MESSAGE 2
async def delete_call_message_2(call):
    try:
        await bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id)
        await bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id - 1)
    except:
        pass

#  DELETE MESSAGE 3
async def delete_call_message_3(call):
    try:
        await bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id)
        await bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id - 1)
        await bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id - 2)
    except:
        pass



#  ON START UP
async def start_bot(_):
    await bot.send_message(284929331, 'The bot is successfully enabled ✅')



#  LAUNCH THE BOT
if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dp, skip_updates = True, on_startup = start_bot)
        except Exception as e:
            print(e)
            continue
