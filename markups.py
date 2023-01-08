from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# TODO конпки проверки подписки
btnUrlChannel = InlineKeyboardButton(text="Подписаться", url="https://t.me/+MUv8UncVDSM3NDYy")
btnDoneSub = InlineKeyboardButton(text="Подписался", callback_data="subChannelDone")
checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnDoneSub)

# TODO конпки главного меню
btnProfile = KeyboardButton('Профиль')
btnSub = KeyboardButton('Подписка')
btnOpportunities = KeyboardButton('Что умеет этот бот?')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnSub, btnProfile, btnOpportunities)

# TODO конпки функционала
btnHistory = KeyboardButton('История')
btnGameElements = KeyboardButton('Игровые элементы')
btnNBA = KeyboardButton('NBA')
btnVTB = KeyboardButton('ВТБ')
btnBack = KeyboardButton('Назад в главное меню')
btnTableNba = KeyboardButton('Турнирная таблица')
btnOnlineNba = KeyboardButton("Записи трансляций NBA")
btnTeamCompositionNba = KeyboardButton("Командные составы NBA")
btnOnlineVtb = KeyboardButton("Прямая трансляций ВТБ")
btnNews = KeyboardButton('Последние новости NBA')
btnPlayerDay = KeyboardButton('Игроки дня по очкам')
btnYouTube = KeyboardButton("Найти видео на YouTube")
btnMusic = KeyboardButton('Музыкальные сборник')
functionalFreeMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
functionalSubMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
functionalFreeMenu.add(btnHistory, btnGameElements, btnNBA, btnVTB, btnBack)
functionalSubMenu.add(btnHistory, btnGameElements, btnNBA, btnVTB,
                      btnTableNba, btnOnlineNba, btnOnlineVtb, btnYouTube, btnTeamCompositionNba, btnPlayerDay, btnNews, btnMusic, btnBack)

# TODO конпки nba
btnResultNba = InlineKeyboardButton('NBA', callback_data="team_position_nba")
btnResultVtb = InlineKeyboardButton('ВТБ', callback_data="team_position_vtb")
resultMenu = InlineKeyboardMarkup(row_width=1)
resultMenu.insert(btnResultNba)
resultMenu.insert(btnResultVtb)

# TODO конпки игровых элементов
btnPerevod = KeyboardButton('Перевод мяча на другую руку')
btnPivot = KeyboardButton('Пивот')
btnPerevodSpina = KeyboardButton('Перевод за спиной')
btnPerevodNogi = KeyboardButton('Перевод мяча между ног')
btnStepBack = KeyboardButton('StepBack')
btnEuroStep = KeyboardButton('EuroStep')
btnBackFunctionalMenu = KeyboardButton('Назад')
GameElementsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
GameElementsMenu.add(btnPerevod, btnPivot, btnPerevodSpina, btnPerevodNogi, btnStepBack, btnEuroStep, btnBackFunctionalMenu)

# TODO конпки для оплаты подписки
sub_inline_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnSubSber = KeyboardButton(text="Сбербанк")
btnSubYKassa = KeyboardButton(text="ЮКасса")
sub_inline_markup.add(btnSubSber, btnSubYKassa, btnBack)

# TODO конпки для оплаты подписки YKassa
btnSubWeekYKassa = InlineKeyboardButton(text="Неделя - 99 рублей", callback_data="subweekykassa")
btnSubMonthYKassa = InlineKeyboardButton(text="Месяц - 499 рублей", callback_data="submonthykassa")
btnSubYearYKassa = InlineKeyboardButton(text="Год - 999 рублей", callback_data="subyearykassa")
sub_inline_markup_ykassa = InlineKeyboardMarkup(row_width=1)
sub_inline_markup_ykassa.insert(btnSubWeekYKassa)
sub_inline_markup_ykassa.insert(btnSubMonthYKassa)
sub_inline_markup_ykassa.insert(btnSubYearYKassa)

# TODO конпки для оплаты подписки Сбербанк
btnSubWeekSber = InlineKeyboardButton(text="Неделя - 99 рублей", callback_data="subweeksber")
btnSubMonthSber = InlineKeyboardButton(text="Месяц - 499 рублей", callback_data="submonthsber")
btnSubYearSber = InlineKeyboardButton(text="Год - 999 рублей", callback_data="subyearsber")
sub_inline_markup_sber = InlineKeyboardMarkup(row_width=1)
sub_inline_markup_sber.insert(btnSubWeekSber)
sub_inline_markup_sber.insert(btnSubMonthSber)
sub_inline_markup_sber.insert(btnSubYearSber)



