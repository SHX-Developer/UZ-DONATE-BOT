from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



#  Register Language
register_language = InlineKeyboardMarkup()
register_language.row(InlineKeyboardButton(text = "🇺🇿  O'zbekcha", callback_data = "reg_uz"),
                      InlineKeyboardButton(text = "🇷🇺  Русский", callback_data = "reg_ru"))

#  Register Currency
register_currency = InlineKeyboardMarkup()
register_currency.row(InlineKeyboardButton(text = '🇺🇿  UZS', callback_data = 'reg_uzs'),
                      InlineKeyboardButton(text = '🇷🇺  RUB', callback_data = 'reg_rub'))




#  Menu (RU)
ru_menu = InlineKeyboardMarkup()
ru_menu.row(InlineKeyboardButton(text = "💎  Задонатить", callback_data = "donate"))
ru_menu.row(InlineKeyboardButton(text = "🆘  Связаться", callback_data = "contact"),
            InlineKeyboardButton(text = "♻️  Обменник", callback_data = "exchange"))
ru_menu.row(InlineKeyboardButton(text = "💸  Валюта", callback_data = "currency"),
            InlineKeyboardButton(text = "🌐  Язык", callback_data = "language"))

#  Menu (UZ)
uz_menu = InlineKeyboardMarkup()
uz_menu.row(InlineKeyboardButton(text = "💎  Donat", callback_data = "donate"))
uz_menu.row(InlineKeyboardButton(text = "🆘  Bog'lanish", callback_data = "contact"),
            InlineKeyboardButton(text = "♻️  Almashtirgich", callback_data = "exchange"))
uz_menu.row(InlineKeyboardButton(text = "💸  Valyuta", callback_data = "currency"),
            InlineKeyboardButton(text = "🌐  Til", callback_data = "language"))





#  Contact (RU)
ru_contact = InlineKeyboardMarkup()
ru_contact.row(InlineKeyboardButton(text = "✅  Донатер", url = 'https://t.me/CyberDonater'))
ru_contact.row(InlineKeyboardButton(text = "📢  Канал", url = 'https://t.me/mobile_mlbb_legends'),
               InlineKeyboardButton(text = "👥  Группа", url = 'https://t.me/MLBBCommunityyy'))
ru_contact.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))

#  Contact (UZ)
uz_contact = InlineKeyboardMarkup()
uz_contact.row(InlineKeyboardButton(text = "✅  Donater", url = 'https://t.me/CyberDonater'))
uz_contact.row(InlineKeyboardButton(text = "📢  Kanal", url = 'https://t.me/mobile_mlbb_legends'),
               InlineKeyboardButton(text = "👥  Guruh", url = 'https://t.me/MLBBCommunityyy'))
uz_contact.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_menu"))





#  Games (RU)
ru_games = InlineKeyboardMarkup()
ru_games.row(InlineKeyboardButton(text = "Mobile Legends",callback_data = 'mobile_legends'),
             InlineKeyboardButton(text = "Pubg",callback_data = 'pubg'))
ru_games.row(InlineKeyboardButton(text = "Free Fire",callback_data = 'free_fire'),
             InlineKeyboardButton(text = "Clash Of Clans",callback_data = 'clash_of_clans'))
ru_games.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))

#  Games (UZ)
uz_games = InlineKeyboardMarkup()
uz_games.row(InlineKeyboardButton(text = "Mobile Legends",callback_data = 'mobile_legends'),
             InlineKeyboardButton(text = "Pubg",callback_data = 'pubg'))
uz_games.row(InlineKeyboardButton(text = "Free Fire",callback_data = 'free_fire'),
             InlineKeyboardButton(text = "Clash Of Clans",callback_data = 'clash_of_clans'))
uz_games.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_menu"))





#  Mobile Legends (RU)
ru_mobile_legends = InlineKeyboardMarkup()
ru_mobile_legends.row(InlineKeyboardButton(text = "💎 8", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 35", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 88", url = 'https://t.me/CyberDonater'))
ru_mobile_legends.row(InlineKeyboardButton(text = "💎 132", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 264", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 440", url = 'https://t.me/CyberDonater'))
ru_mobile_legends.row(InlineKeyboardButton(text = "💎 734", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 933", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 1410", url = 'https://t.me/CyberDonater'))
ru_mobile_legends.row(InlineKeyboardButton(text = "💎 1881", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 2845", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 6163", url = 'https://t.me/CyberDonater'))
ru_mobile_legends.row(InlineKeyboardButton(text = "🏷  Weekly Pass", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "🏷  Twilight Pass", url = 'https://t.me/CyberDonater'))
ru_mobile_legends.row(InlineKeyboardButton(text = "💳  Заказать", url = 'https://t.me/CyberDonater'))
ru_mobile_legends.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))

#  Mobile Legends (UZ)
uz_mobile_legends = InlineKeyboardMarkup()
uz_mobile_legends.row(InlineKeyboardButton(text = "💎 8", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 35", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 88", url = 'https://t.me/CyberDonater'))
uz_mobile_legends.row(InlineKeyboardButton(text = "💎 132", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 264", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 440", url = 'https://t.me/CyberDonater'))
uz_mobile_legends.row(InlineKeyboardButton(text = "💎 734", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 933", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 1410", url = 'https://t.me/CyberDonater'))
uz_mobile_legends.row(InlineKeyboardButton(text = "💎 1881", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 2845", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "💎 6163", url = 'https://t.me/CyberDonater'))
uz_mobile_legends.row(InlineKeyboardButton(text = "🏷  Weekly Pass", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "🏷  Twilight Pass", url = 'https://t.me/CyberDonater'))
uz_mobile_legends.row(InlineKeyboardButton(text = "💳  Buyurtma berish", url = 'https://t.me/CyberDonater'))
uz_mobile_legends.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_games"))



#  Pubg (RU)
ru_pubg = InlineKeyboardMarkup()
ru_pubg.row(InlineKeyboardButton(text = "💵 60", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 325", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 660", url = 'https://t.me/CyberDonater'))
ru_pubg.row(InlineKeyboardButton(text = "💵 1800", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 3850", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "💵 8100", url = 'https://t.me/CyberDonater'))
ru_pubg.row(InlineKeyboardButton(text = "🏷  RP", url = 'https://t.me/CyberDonater'),
         InlineKeyboardButton(text = "🏷  Elite RP", url = 'https://t.me/CyberDonater'))
ru_pubg.row(InlineKeyboardButton(text = "💳  Заказать", url = 'https://t.me/CyberDonater'))
ru_pubg.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))

#  Pubg (UZ)
uz_pubg = InlineKeyboardMarkup()
uz_pubg.row(InlineKeyboardButton(text = "💵 60", url = 'https://t.me/CyberDonater'),
            InlineKeyboardButton(text = "💵 325", url = 'https://t.me/CyberDonater'),
            InlineKeyboardButton(text = "💵 660", url = 'https://t.me/CyberDonater'))
uz_pubg.row(InlineKeyboardButton(text = "💵 1800", url = 'https://t.me/CyberDonater'),
            InlineKeyboardButton(text = "💵 3850", url = 'https://t.me/CyberDonater'),
            InlineKeyboardButton(text = "💵 8100", url = 'https://t.me/CyberDonater'))
uz_pubg.row(InlineKeyboardButton(text = "🏷  RP", url = 'https://t.me/CyberDonater'),
            InlineKeyboardButton(text = "🏷  Elite RP", url = 'https://t.me/CyberDonater'))
uz_pubg.row(InlineKeyboardButton(text = "💳  Buyurtma berish", url = 'https://t.me/CyberDonater'))
uz_pubg.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_games"))



#  Free Fire  (RU)
ru_free_fire = InlineKeyboardMarkup()
ru_free_fire.row(InlineKeyboardButton(text = "💎 100", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 210", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 530", url = 'https://t.me/CyberDonater'))
ru_free_fire.row(InlineKeyboardButton(text = "💎 645", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 1080", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 2200", url = 'https://t.me/CyberDonater'))
ru_free_fire.row(InlineKeyboardButton(text = "💎 4450", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 6900", url = 'https://t.me/CyberDonater'))
ru_free_fire.row(InlineKeyboardButton(text = "💳  Заказать", url = 'https://t.me/CyberDonater'))
ru_free_fire.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))

#  Free Fire  (UZ)
uz_free_fire = InlineKeyboardMarkup()
uz_free_fire.row(InlineKeyboardButton(text = "💎 100", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 210", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 530", url = 'https://t.me/CyberDonater'))
uz_free_fire.row(InlineKeyboardButton(text = "💎 645", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 1080", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 2200", url = 'https://t.me/CyberDonater'))
uz_free_fire.row(InlineKeyboardButton(text = "💎 4450", url = 'https://t.me/CyberDonater'),
                 InlineKeyboardButton(text = "💎 6900", url = 'https://t.me/CyberDonater'))
uz_free_fire.row(InlineKeyboardButton(text = "💳  Buyurtma berish", url = 'https://t.me/CyberDonater'))
uz_free_fire.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_games"))



#  Clash Of Clans (RU)
ru_clash_of_clans = InlineKeyboardMarkup()
ru_clash_of_clans.row(InlineKeyboardButton(text = "❇️ 88", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 550", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 1320", url = 'https://t.me/CyberDonater'))
ru_clash_of_clans.row(InlineKeyboardButton(text = "❇️ 2750", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 7150", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 15400", url = 'https://t.me/CyberDonater'))
ru_clash_of_clans.row(InlineKeyboardButton(text = "🏷 Gold Pass", url = 'https://t.me/CyberDonater'))
ru_clash_of_clans.row(InlineKeyboardButton(text = "💳 Заказать", url = 'https://t.me/CyberDonater'))
ru_clash_of_clans.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_games"))

#  Clash Of Clans (UZ)
uz_clash_of_clans = InlineKeyboardMarkup()
uz_clash_of_clans.row(InlineKeyboardButton(text = "❇️ 88", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 550", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 1320", url = 'https://t.me/CyberDonater'))
uz_clash_of_clans.row(InlineKeyboardButton(text = "❇️ 2750", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 7150", url = 'https://t.me/CyberDonater'),
                      InlineKeyboardButton(text = "❇️ 15400", url = 'https://t.me/CyberDonater'))
uz_clash_of_clans.row(InlineKeyboardButton(text = "🏷 Gold Pass", url = 'https://t.me/CyberDonater'))
uz_clash_of_clans.row(InlineKeyboardButton(text = "💳  Buyurtma berish", url = 'https://t.me/CyberDonater'))
uz_clash_of_clans.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_games"))





#  Exchange (RU)
ru_exchange = InlineKeyboardMarkup()
ru_exchange.row(InlineKeyboardButton(text = "♻️  Обменять", url = 'https://t.me/CyberDonater'))
ru_exchange.row(InlineKeyboardButton(text = "<<  Назад", callback_data = "back_menu"))

#  Exchange (UZ)
uz_exchange = InlineKeyboardMarkup()
uz_exchange.row(InlineKeyboardButton(text = "♻️  Almashtirish", url = 'https://t.me/CyberDonater'))
uz_exchange.row(InlineKeyboardButton(text = "<<  Orqaga", callback_data = "back_menu"))

