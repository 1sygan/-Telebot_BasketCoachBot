import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
import markups as nav
from db import Database
from text import *
import time
import datetime
import functions as fc


TOKEN = "5959698761:AAEWO64P_G_b3geLr8sO6YWDyze941rOtWA"
YOOTOKEN = "381764678:TEST:46698"
CHANNEL_ID = "-1001545665727"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


def days_to_seconds(days):
    return days * 24 * 60 * 60


def time_sub_day(get_time):
    time_now = int(time.time())
    middle_time = int(get_time) - time_now
    if middle_time <= 0:
        return False
    else:
        dt = str(datetime.timedelta(seconds=middle_time))
        dt = dt.replace("days", "дней")
        dt = dt.replace("day", "день")
        return dt

# старт бота, регистрация
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет!")
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            await bot.send_message(message.from_user.id, "Укажите ваш ник")
        else:
            if db.get_nickname(message.from_user.id) == "None":
                await bot.send_message(message.from_user.id, "Укажите ваш ник")
            else:
                await bot.send_message(message.from_user.id, "Вы уже зарегистированы!", reply_markup=nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Для доступа у функционалу бота, подпишитесь на канал", reply_markup=nav.checkSubMenu)

# проверка подписки на канал
@dp.callback_query_handler(text="subChannelDone")
async def sub_channel_done(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет!")
    else:
        await bot.send_message(message.from_user.id, "Для доступа у функционалу бота, подпишитесь на канал BasketNews", reply_markup=nav.checkSubMenu)

# основной функционал бота
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            if message.text == "Профиль":
                user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)
                user_sub = time_sub_day(db.get_time_sub(message.from_user.id))
                if user_sub == False:
                    user_sub = "Нет"
                user_sub = "\nПодписка: " + user_sub
                await bot.send_message(message.from_user.id, user_nickname + user_sub)
            elif message.text == "Подписка":
                await bot.send_message(message.from_user.id, sub_text, reply_markup=nav.sub_inline_markup)


            elif message.text =="Что умеет этот бот?":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, functional_sub_text, reply_markup=nav.functionalSubMenu)
                else:
                    await bot.send_message(message.from_user.id, functional_free_text, reply_markup=nav.functionalFreeMenu)
            # без подписки
            elif message.text == "История":
                await bot.send_photo(message.chat.id,
                                     r'https://metaratings.ru/upload/sprint.editor/c8e/c8e72238f44552cb93f0cf7ba1743fde.jpg', caption=history_text)
            elif message.text =="Игровые элементы":
                await bot.send_message(message.chat.id, general_element_text, reply_markup=nav.GameElementsMenu)
            elif message.text == "Перевод мяча на другую руку":
                await bot.send_animation(message.chat.id, 'https://i.pinimg.com/originals/ac/b8/b8/acb8b8cec4011bec35468dff5f8af1f7.gif')
            elif message.text == "Пивот":
                await bot.send_animation(message.chat.id, 'https://i.gifer.com/7hD3.gif')
            elif message.text == "Перевод за спиной":
                await bot.send_animation(message.chat.id, 'https://www.slamdunk.ru/uploads/monthly_2021_04/1504906273_hardenstepback_1x1_v2(1).gif.f3885522652c517af2a9dc4e1e94e3c8.gif')
            elif message.text == "Перевод мяча между ног":
                await bot.send_animation(message.chat.id, 'https://www.slamdunk.ru/uploads/monthly_2021_04/lukastepback_1x1_v3.gif.eff34e96ef0d58cab911eca9d9f03582.gif',
                                         caption="Связка перевода между ног и за спиной")
            elif message.text == "StepBack":
                await bot.send_animation(message.chat.id, 'https://www.slamdunk.ru/uploads/monthly_2019_12/1Fwh9ek.gif.d5523e73a1a9735f3a4d2fdf0cb21f20.gif')
            elif message.text == "EuroStep":
                await bot.send_animation(message.chat.id, 'https://i.gifer.com/5pJm.gif')
            elif message.text == "Назад в главное меню":
                await bot.send_message(message.from_user.id, "Возвращаю главное меню", reply_markup=nav.mainMenu)
            elif message.text == "Назад":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Возвращаю в меню функционала", reply_markup=nav.functionalSubMenu)
                else:
                    await bot.send_message(message.from_user.id, "Возвращаю в меню функционала", reply_markup=nav.functionalFreeMenu)
            elif message.text == "NBA":
                await bot.send_photo(message.chat.id,
                                     r'https://ss.sport-express.ru/userfiles/materials/160/1605423/large.jpg', caption=nba_text)
            elif message.text == "ВТБ":
                await bot.send_photo(message.chat.id,
                                     r'https://vtb-league.com/app/uploads/2021/03/zaglushka.jpg', caption=vtb_text)
            # с подпиской
            elif message.text == "Турнирная таблица":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Тут результативность команд", reply_markup=nav.resultMenu)
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")
            elif message.text == "Записи трансляций NBA":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Тут записи последних трансляций https://nba-tv.info/")
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")
            elif message.text == "Прямая трансляций ВТБ":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Тут прямая трансляция https://vtb-league.com/")
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")
            elif message.text == "Найти видео на YouTube":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, pars_youtube_text)
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")

            elif message.text == 'Музыкальные сборник':
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "https://music.yandex.ru/album/10933999")
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")

            # парсер последних новостей
            elif message.text == 'Последние новости NBA':
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Начинаю поиск новостей")
                    URL = "https://www.sports.ru/nba/news/"
                    sleep(3)
                    response = requests.get(url=URL)
                    soup = bs(response.text, 'html.parser')
                    lastNews = soup.find("div", class_="short-news").text
                    message_to_user = f'Вот что мне удалось найти:\n {lastNews.replace("  ", "")}\nПоcмотреть подробнее : {URL}\n'
                    await bot.send_message(message.from_user.id, message_to_user)
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")

            # парсер игроки дня
            elif message.text == 'Игроки дня по очкам':
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Начинаю поиск игроков")
                    URL = "https://www.sports.ru/nba/stat/"
                    sleep(3)
                    response = requests.get(url=URL)
                    soup = bs(response.text, 'html.parser')
                    allPlayer = ""
                    tablePlayer = soup.find("tbody")
                    for row in tablePlayer.find_all("tr"):
                        playerName = row.find("a").text
                        playerTeam = row.find("td", class_="name-td alLeft bordR").text
                        allPlayer += f'Имя игрока: {playerName.replace("  ", "")}\nКоманда: {playerTeam.replace("  ", "")}\n'
                    await bot.send_message(message.from_user.id, allPlayer)
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")


            elif message.text =="Командные составы NBA":
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, conposition_text)
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")

             # парсер игрового состава
            elif "$" in message.text:
                teams_link_id = fc.recognize_team(message.text, db.get_teams())
                URL = "https://allbasketball.org/teams/" + db.get_teams_link(teams_link_id)
                sleep(3)
                response = requests.get(url=URL)
                soup = bs(response.text, "lxml")
                allPlayer = ""
                teamData = soup.find("tbody")
                for row in teamData.find_all("div", class_="d-flex align-items-center"):
                    playerName = row.find("a", class_="player-name").text
                    playerPosition = row.find("div", class_="player-position").text
                    allPlayer += f'Имя игрока: {playerName.replace("  ", "")}Позиция игрока: {playerPosition.replace("  ", "")}\n'
                await bot.send_message(message.from_user.id, allPlayer)

            # парсер YouTube
            elif "Поиск" in message.text:
                if db.get_sub_status(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Начинаю искать")
                    video_href = "https://www.youtube.com/results?search_query=" + "баскетбол " + message.text[5:]
                    driver.get(video_href)
                    sleep(2)
                    videos = driver.find_elements("id", "video-title")
                    for i in range(len(videos)):
                        await bot.send_message(message.chat.id, videos[i].get_attribute('href'))
                        if i == 5:
                            break
                else:
                    await bot.send_message(message.from_user.id, "Для этого нужно преобрести подписку")
            else:
                if db.get_signup(message.from_user.id) == "setnickname":
                    if(len(message.text)) > 15:
                        await bot.send_message(message.from_user.id, "Никнейм не должен превышать 15 символов")
                    elif '@' in message.text or '%' in message.text or '/' in message.text or '$' in message.text:
                        await bot.send_message(message.from_user.id, "Символы '@', '%', '/', '$' нельзя использовать при регистрации никнейма")
                    else:
                        db.set_nickname(message.from_user.id, message.text)
                        db.set_signup(message.from_user.id, "done")
                        await bot.send_message(message.from_user.id, "Регистрация прошла успепшно!", reply_markup=nav.mainMenu)
                else:
                    await bot.send_message(message.from_user.id, "Я не пониваю вас")
        else:
            await bot.send_message(message.from_user.id, "Для доступа к функционалу бота, подпишитесь на канал",
                                   reply_markup=nav.checkSubMenu)


# парсер NBA команд
@dp.callback_query_handler(text="team_position_nba")
async def parser(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    URL = "https://allbasketball.org/teams/statistics.html"
    sleep(3)
    response = requests.get(url=URL)
    soup = bs(response.text, "lxml")
    allTeams = ""
    teamData = soup.find("tbody")
    for row in teamData.find_all("tr"):
        teamName = row.find("a", class_="team-name").text
        teamDevision = row.find("div", class_="team-division").text
        allTeams += f'Команда: {teamName}Девизион: {teamDevision}\n'
    await bot.send_message(message.from_user.id, allTeams)

# парсер ВТБ команд
@dp.callback_query_handler(text="team_position_vtb")
async def parser(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    URL = "https://news.sportbox.ru/Vidy_sporta/Basketbol/vtb-league/stats"
    sleep(3)
    response = requests.get(url=URL)
    soup = bs(response.text, "lxml")
    allTeams = ""
    teamData = soup.find("tbody")
    for row in teamData.find_all("td", class_="info table-link"):
        teamName = row.find("a").text.replace("  ", "")
        allTeams += f'Команда: {teamName}\n\n'
    await bot.send_message(message.from_user.id, allTeams)

# обработка подписки
@dp.callback_query_handler(text="subweek")
async def sub_week(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки", description=sub_text, payload="week_sub",
                           provider_token=YOOTOKEN, currency="RUB", start_parameter="BasketCoachBot", prices=[{"label": "Руб", "amount": 9999 }])


@dp.callback_query_handler(text="submonth")
async def sub_month(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки", description=sub_text, payload="month_sub",
                           provider_token=YOOTOKEN, currency="RUB", start_parameter="BasketCoachBot", prices=[{"label": "Руб", "amount": 24999 }])


@dp.callback_query_handler(text="subyear")
async def sub_year(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки", description=sub_text, payload="year_sub",
                           provider_token=YOOTOKEN, currency="RUB", start_parameter="BasketCoachBot", prices=[{"label": "Руб", "amount": 99999 }])


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# проверка была ли подписк ранее
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == "week_sub":
        if db.get_time_sub(message.from_user.id) <= int(time.time()):
            time_sub = int(time.time()) + days_to_seconds(7)
            db.set_time_sub(message.from_user.id, time_sub)
            await  bot.send_message(message.from_user.id, "Вам выдана подписка на неделю")
        else:
            time_sub = db.get_time_sub(message.from_user.id) + days_to_seconds(7)
            db.set_time_sub(message.from_user.id, time_sub)
            await  bot.send_message(message.from_user.id, "Ваша подписка продлена на неделю")

    elif message.successful_payment.invoice_payload == "month_sub":
        if db.get_time_sub(message.from_user.id) <= int(time.time()):
            time_sub = int(time.time()) + days_to_seconds(30)
            db.set_time_sub(message.from_user.id, time_sub)
            await  bot.send_message(message.from_user.id, "Вам выдана подписка на месяц")
        else:
            time_sub = db.get_time_sub(message.from_user.id) + days_to_seconds(30)
            db.set_time_sub(message.from_user.id, time_sub)
            await  bot.send_message(message.from_user.id, "Ваша подписка продлена на месяц")

    elif message.successful_payment.invoice_payload == "year_sub":
        if db.get_time_sub(message.from_user.id) <= int(time.time()):
            time_sub = int(time.time()) + days_to_seconds(365)
            db.set_time_sub(message.from_user.id, time_sub)
            await  bot.send_message(message.from_user.id, "Вам выдана подписка на год")
        else:
            time_sub = db.get_time_sub(message.from_user.id) + days_to_seconds(365)
            db.set_time_sub(message.from_user.id, time_sub)
            await  bot.send_message(message.from_user.id, "Ваша подписка продлена на год")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


