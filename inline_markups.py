from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



#  Menu
menu = InlineKeyboardMarkup()
menu.row(InlineKeyboardButton(text = "💎  Задонатить", callback_data = "donate"))
menu.row(InlineKeyboardButton(text = "🆘  Связаться", callback_data = "contact"),
         InlineKeyboardButton(text = "♻️  Обменник", callback_data = "exchange"))
menu.row(InlineKeyboardButton(text = "💸  Валюта", callback_data = "currency"),
         InlineKeyboardButton(text = "🌐  Язык", callback_data = "language"))



#  Games
games = InlineKeyboardMarkup()
games.row(InlineKeyboardButton(text = "Mobile Legends",callback_data = 'mobile_legends'),
          InlineKeyboardButton(text = "Pubg",callback_data = 'pubg'))
games.row(InlineKeyboardButton(text = "Free Fire",callback_data = 'free_fire'),
          InlineKeyboardButton(text = "Clash Of Clans",callback_data = 'clash_of_clans'))
games.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))



#  Mobile Legends
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
mobile_legends.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))



#  Pubg
pubg = InlineKeyboardMarkup()
pubg.row(InlineKeyboardButton(text = "💵 60", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 325", url = 'https://t.me/CyberDonater'))
pubg.row(InlineKeyboardButton(text = "💵 660", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 1800", url = 'https://t.me/CyberDonater'))
pubg.row(InlineKeyboardButton(text = "💵 3850", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 8100", url = 'https://t.me/CyberDonater'))
pubg.row(InlineKeyboardButton(text = "💵 RP", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 Elite RP", url = 'https://t.me/CyberDonater'))
pubg.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))



#  Free Fire
free_fire = InlineKeyboardMarkup()
free_fire.row(InlineKeyboardButton(text = "💎 100", url = 'https://t.me/CyberDonater'),
              InlineKeyboardButton(text = "💎 210", url = 'https://t.me/CyberDonater'))
free_fire.row(InlineKeyboardButton(text = "💎 530", url = 'https://t.me/CyberDonater'),
              InlineKeyboardButton(text = "💎 645", url = 'https://t.me/CyberDonater'))
free_fire.row(InlineKeyboardButton(text = "💎 1080", url = 'https://t.me/CyberDonater'),
              InlineKeyboardButton(text = "💎 2200", url = 'https://t.me/CyberDonater'))
free_fire.row(InlineKeyboardButton(text = "💎 4450", url = 'https://t.me/CyberDonater'),
              InlineKeyboardButton(text = "💎 6900", url = 'https://t.me/CyberDonater'))
free_fire.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))



#  Clash Of Clans
clash_of_clans = InlineKeyboardMarkup()
clash_of_clans.row(InlineKeyboardButton(text = "❇️ 88", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "❇️ 550", url = 'https://t.me/CyberDonater'))
clash_of_clans.row(InlineKeyboardButton(text = "❇️ 1320", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "❇️ 2750", url = 'https://t.me/CyberDonater'))
clash_of_clans.row(InlineKeyboardButton(text = "❇️ 7150", url = 'https://t.me/CyberDonater'),
                   InlineKeyboardButton(text = "❇️ 15400", url = 'https://t.me/CyberDonater'))
clash_of_clans.row(InlineKeyboardButton(text = "❇️ Gold Pass", url = 'https://t.me/CyberDonater'))
clash_of_clans.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))




#  Exchange
exchange = InlineKeyboardMarkup()
exchange.row(InlineKeyboardButton(text = "Обменять", url = 'https://t.me/CyberDonater'))
exchange.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))





#  Currency
currency = InlineKeyboardMarkup()
currency.row(InlineKeyboardButton(text = "UZS", callback_data = 'uzs'),
             InlineKeyboardButton(text = "RUB", callback_data = "rub"),
             InlineKeyboardButton(text = "USD", callback_data = "usd"))
currency.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))


language = InlineKeyboardMarkup()
language.row(InlineKeyboardButton(text = "Uzbek", callback_data = 'uzbek'),
             InlineKeyboardButton(text = "Русский", callback_data = "russian"),
             InlineKeyboardButton(text = "English", callback_data = "english"))
language.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))