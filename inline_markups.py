from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



#  INLINE
menu = InlineKeyboardMarkup()
menu.row(InlineKeyboardButton(text = "💎  Задонатить", callback_data = "donate"))
menu.row(InlineKeyboardButton(text = "🎮  Игры", callback_data = "games"),
         InlineKeyboardButton(text = "💸  Обменник", callback_data = "exchange"))
menu.row(InlineKeyboardButton(text = "🆘  Связаться", callback_data = "contact"),
         InlineKeyboardButton(text = "🌐  Язык", callback_data = "language"))


exchange = InlineKeyboardMarkup()
exchange.row(InlineKeyboardButton(text = "Обменять", url = 'https://t.me/CyberDonater'))
exchange.row(InlineKeyboardButton(text = "Назад", callback_data = "back"))
