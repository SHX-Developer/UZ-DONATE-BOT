from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import sqlite3
import datetime

import config
import inline_markups
import reply_markups





#  LIBRARY VARIABLES

storage = MemoryStorage()

bot = Bot(config.token)
dp = Dispatcher(bot, storage = MemoryStorage())

db = sqlite3.connect('database.db', check_same_thread = False)
sql = db.cursor()

date_time = datetime.datetime.now().date()



#  STATES

class States(StatesGroup):
    value = State()



#  CREATING DATABASE
sql.execute('CREATE TABLE IF NOT EXISTS user_access (id INTEGER, username TEXT, firstname TEXT, lastname TEXT, date DATE)')
db.commit()




mobile_legends_prices = '''
💎  8  -  1.500 uzs  (11 ₽)
💎  35  -  6.000 сум  (44 ₽)
💎  88  -  15.000 сум  (109 ₽) 
💎  132  -  22.000 сум  (160 ₽)
💎  264  -  43.000 сум  (312 ₽)
💎  440  -  72.000 сум  (522 ₽)
💎  734  -  115.000 сум  (834 ₽)
💎  933  -  137.000 сум  (994 ₽)
💎  1410  -  215.000 сум  (1559 ₽)
💎  1881  -  288.000 сум  (2089 ₽)
💎  2845  -  420.000  сум  (3045 ₽)
💎  6163  -  875.000 сум  (6344 ₽)
💎  WeeklyPass -18.000 сум (130₽)

💳  8600120453183769
💳  9860160104516572
💳  4231200009317065

🙋‍♂️  Донатер - @CyberDonater

✈️  Наш телеграм канал (https://t.me/mobile_mlbb_legends)
'''

pubg_prices = '''
60 UC  -  (91 ₽)
325 UC  -  (440 ₽)
660 UC  -  (910 ₽)
1800 UC  -  (2248 ₽)
3850 UC  -  (4500 ₽)
8100 UC  -  (9100 ₽)
RP Upgrade Pack A3  -  (1442 ₽)
Elite RP Upgrade Pack A3  -  (3608 ₽)

💳  8600120453183769
💳  9860160104516572
💳  4231200009317065

🙋‍♂️  Донатер - @CyberDonater

✈️  Наш телеграм канал (https://t.me/mobile_mlbb_legends)
'''


free_fire_prices = '''
💎  100  -  (113 ₽)
💎  210  -  (127 ₽)
💎  530  -  (568 ₽)
💎  645  -  (761 ₽)
💎  1080  -  (1136 ₽)
💎  2200  -  (2272 ₽)
💎  4450  -  (5061 ₽)
💎  6900  -  (7592 ₽)

💳  8600120453183769
💳  9860160104516572
💳  4231200009317065

🙋‍♂️  Донатер - @CyberDonater

✈️  Наш телеграм канал (https://t.me/mobile_mlbb_legends)
'''


clash_of_clans_prices = '''
💎  88  -  (101 ₽)
💎  550  -  (511 ₽)
💎  1320  -  (1022 ₽)
💎  2750  -  (2047 ₽)
💎  7150  -  (5119 ₽)
💎  15400  -  (10239 ₽)
💎  Gold Pass  -  (715 ₽)

💳  8600120453183769
💳  9860160104516572
💳  4231200009317065

🙋‍♂️  Донатер - @CyberDonater

✈️  Наш телеграм канал (https://t.me/mobile_mlbb_legends)
'''



#  START COMMAND

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    sql.execute('SELECT id FROM user_access WHERE id = ?', (message.chat.id,))
    user_id = sql.fetchone()

    if user_id == None:
        sql.execute('INSERT INTO user_access (id, username, firstname, lastname, date) VALUES (?, ?, ?, ?, ?)',
        (message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, date_time))
        db.commit()

        await bot.send_message(message.chat.id, '<b> Welcome ! </b>', parse_mode = 'html', reply_markup = None)

    else:
        await bot.send_message(message.chat.id, '<b> Main menu: </b>', parse_mode = 'html', reply_markup = None)





#  TEXT

@dp.message_handler()
async def text(message: types.Message):
    
    if message.text == 'TEXT':
        await bot.send_message(message.chat.id, '<b> TEXT </b>', parse_mode = 'html', reply_markup = None)

    elif message.text == 'TEXT':
        await bot.send_message(message.chat.id, '<b> TEXT </b>', parse_mode = 'html', reply_markup = None)

    elif message.text == 'TEXT':
        await bot.send_message(message.chat.id, '<b> TEXT </b>', parse_mode = 'html', reply_markup = None)

    else:
        await bot.send_message(message.chat.id, '<b> TEXT </b>', parse_mode = 'html', reply_markup = None)





#  CALLBACK
@dp.callback_query_handler(lambda call: True)
async def callback_queries(call: types.CallbackQuery):


#  SEND MESSAGE
    if call.data == 'callback_1':
        await bot.send_message(
            chat_id =call.message.chat.id, 
            text = '<b> TEXT </b>', 
            parse_mode = 'html', 
            reply_markup = None)


#  DELETE INLINE MESSAGE
    elif call.data == 'delete_inline':
        await bot.delete_message(
            chat_id = call.message.chat.id, 
            message_id = call.message.message_id)


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
        with open('photo/photo.jpg', 'rb') as photo:
            bot.edit_message_media( 
                media = types.InputMedia(
                type = 'photo',
                media = photo,
                chat_id = call.message.chat.id,
                message_id = call.message.message_id,
                caption = '<b> TEXT </b>',
                parse_mode = 'html'),
                reply_markup = None)




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