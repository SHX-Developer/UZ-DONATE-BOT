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
exchange.row(InlineKeyboardButton(text = "Назад", callback_data = "back_menu"))


games = InlineKeyboardMarkup()
games.row(InlineKeyboardButton(text = "Mobile Legends",callback_data = 'mobile_legends'),
          InlineKeyboardButton(text = "Pubg",callback_data = 'pubg'))
games.row(InlineKeyboardButton(text = "Free Fire",callback_data = 'free_fire'),
          InlineKeyboardButton(text = "Clash Of Clans",callback_data = 'clash_of_clans'))
games.row(InlineKeyboardButton(text = "Назад", callback_data = "back_menu"))


mobile_legends = InlineKeyboardMarkup()
mobile_legends.row(InlineKeyboardButton(text = "💎 8", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "💎 35", url = 'https://t.me/CyberDonater'))
mobile_legends.row(InlineKeyboardButton(text = "💎 88", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "💎 132", url = 'https://t.me/CyberDonater'))
mobile_legends.row(InlineKeyboardButton(text = "💎 264", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "💎 440", url = 'https://t.me/CyberDonater'))
mobile_legends.row(InlineKeyboardButton(text = "💎 734", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "💎 933", url = 'https://t.me/CyberDonater'))
mobile_legends.row(InlineKeyboardButton(text = "💎 1410", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "💎 1881", url = 'https://t.me/CyberDonater'))
mobile_legends.row(InlineKeyboardButton(text = "💎 2845", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "💎 6163", url = 'https://t.me/CyberDonater'))

mobile_legends.row(InlineKeyboardButton(text = "Назад", callback_data = "back_menu"))