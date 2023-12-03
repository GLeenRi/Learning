from multiprocessing.resource_sharer import stop
import telebot
import sqlite3
import random
import time
import requests
import pathlib
import os
from pathlib import Path
## help(telebot)
from pathlib import *
import pathlib

current_dir = pathlib.Path.cwd()
from pathlib import Path


dlk = pathlib.Path.home() / 'DLK' / 'DLK_01.jpg'

home_dir = pathlib.Path.home()
print(current_dir)
print(home_dir)
print(dlk)

from telebot import types
from datetime import date
today = date.today()
from time import sleep
from peewee import *
TOKEN = "112" ## вместо 112 your TOKEN


db = SqliteDatabase('Shokolad.db')
class User(Model):
    user_id = TextField()
    rang = IntegerField(default=0)
    start = IntegerField(default=0)
    


    class Meta:
        database = db
        db_table = 'users'
User.create_table()
def does_it_exist(model, instance):
    exits = model.select().where(model.user_id == instance)
    if not bool(exits):
        return True
    else:
        return False

def reg_DB(uid):
    if not does_it_exist(User, uid):
        user = User.get(User.user_id == uid)
        user.save()

    else:
        print('I')
        usersDB = User(user_id = uid)
        usersDB.save()


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    reg_DB(message.from_user.id)
    user = User.get(User.user_id == message.from_user.id)
    start = User.get(User.user_id == message.from_user.id).start
    if start <= 0:
        user.start +=1;
        user.save()
        print(user)
        bot.send_message(message.chat.id, 'Регистрирую в системе...')
        bot.send_message(message.chat.id,  message.from_user.id )
        print(f"{message.from_user.id}")
        bot.send_message(message.chat.id, 'Привет, работник шоколада')
        bot.send_message(message.chat.id, 'У меня есть команды для разных позиций /commands')

    else:
        print(message.from_user.id)
        bot.send_message(message.chat.id, 'Проверяю в системе...')
        bot.send_message(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, 'У меня есть команды для разных позиций /commands')


@bot.message_handler(commands=['commands'])
def commands(message):
    user = User.get(User.user_id == message.from_user.id)
    print(f"commands {user}")
    markup1 = types.InlineKeyboardMarkup(row_width=1)
    item_Kitchen = types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Кухня кнопка
    item_C = types.InlineKeyboardButton('Прилавок', callback_data='C') ## Прилавок кнопка
    item_hospitality = types.InlineKeyboardButton('Гостепреимство 2.0', callback_data='hospitality') ## Гостепреимство кнопка
    item_DLK = types.InlineKeyboardButton('Доcтавка Модули', callback_data='DLK') ## Доставка Кнопка
    markup1.add(item_Kitchen,item_C,item_hospitality,item_DLK)
    bot.send_message(message.chat.id, 'Список модулей -->', reply_markup=markup1)
    

    

@bot.callback_query_handler(func =lambda call:True)
def kitchen_button_press(call):
    if call.message:
        if call.data == "Kitchen":
                print(f"kitchen {call.from_user.id}")
                markup = types.InlineKeyboardMarkup(row_width=2)
                item_grille = types.InlineKeyboardButton('Гриль', callback_data='Grille_01') ## Булочки Обед
                item_grille_moning = types.InlineKeyboardButton('Гриль Утро', callback_data='Grille_02') ## Булочки Обед
                item_friture = types.InlineKeyboardButton('Фритюр', callback_data='Friture_02') ## Булочки Обед
                item_friture_moning = types.InlineKeyboardButton('Фритюр Утро', callback_data='Friture_01') ## Булочки Обед
                item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
                item_bulochki_breakfest= types.InlineKeyboardButton('Булочки Завтрак', callback_data='Bul_BR2') ## Булочки Завтрак
                markup.add(item_bulochki_obed,item_grille,item_friture,item_bulochki_breakfest,item_grille_moning,item_friture_moning)
                bot.send_message(call.message.chat.id, '/commands', reply_markup=markup)
                

    if call.message:
        if call.data == 'Bul_OB1':
            print(f"recept_obed{call.from_user.id}")
            markup01 = types.InlineKeyboardMarkup(row_width=2)
            item_Cheese = types.InlineKeyboardButton('Чизбургер', callback_data='Obed_Cheese') ## Чизбургер
            item_Hamburger= types.InlineKeyboardButton('Гамбургер', callback_data='Obed_Hamburger') ## Гамбургер
            item_Burger = types.InlineKeyboardButton('Чикенбургер', callback_data='Obed_Burger') ## 
            item_Double_Cheese = types.InlineKeyboardButton('Двойной \n Чизбургер', callback_data='Obed_Double_Cheese') ## 
            
            markup02 = types.InlineKeyboardMarkup(row_width=2)
            item_Grand = types.InlineKeyboardButton('Гранд', callback_data='Obed_Grand') ## 
            item_DoubleGrand = types.InlineKeyboardButton('Двойной Гранд', callback_data='Obed_Double_Grand') ## 
            item_GrandDeluxe = types.InlineKeyboardButton('Гранд ДеЛюкс', callback_data='Obed_Grand_Deluxe') ## 
            item_Premier = types.InlineKeyboardButton('Премьер', callback_data='Obed_Premier') ## 
            

            markup03 = types.InlineKeyboardMarkup(row_width=2)            
            item_BigSpeshl= types.InlineKeyboardButton('Биг \n Спешл', callback_data='Obed_Speshl') ## 
            item_3xSpeshl= types.InlineKeyboardButton('Биг \n Спешл \n 3 Сыра', callback_data='Obed_Speshlx3') ## 
            item_Double_Speshl= types.InlineKeyboardButton('Дв \n Биг \n Спешл', callback_data='Obed_Double_Speshl') ## 
            item_Chiken_Hit= types.InlineKeyboardButton('Чикен \n Хит \n ', callback_data='Obed_Chiken_Hit') ## 
            markup04 = types.InlineKeyboardMarkup(row_width=2)
            item_FishBurger= types.InlineKeyboardButton('Фиш \n Бургер', callback_data='Obed_FishBurger') ## 
            item_Double_FishBurger= types.InlineKeyboardButton('Двойной \n Фиш \n Бургер', callback_data='Obed_Double_FishBurger') ## 
            markup05 = types.InlineKeyboardMarkup(row_width=3)
            item_CezarRoll= types.InlineKeyboardButton('Цезарь \n Ролл', callback_data='Obed_Cezar_Roll') ## 
            item_CezarRoll_Becon= types.InlineKeyboardButton('Цезарь Ролл Бекон', callback_data='Obed_Cezar_Becon') ## 
            
            item_Shrimp_Roll= types.InlineKeyboardButton('Креветка \n Ролл ', callback_data='Obed_Shrimp_Roll') ## 
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            item_Kitchen = types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Кухня кнопка
            
            markup01.add(item_Cheese, item_Hamburger,item_Burger, item_Double_Cheese,)
            markup02.add(item_Grand, item_DoubleGrand, item_GrandDeluxe,)
            markup03.add(item_Premier, item_BigSpeshl, item_Double_Speshl, item_3xSpeshl,item_Chiken_Hit)
            markup04.add(item_FishBurger, item_Double_FishBurger)
            markup05.add(item_CezarRoll, item_CezarRoll_Becon, item_Shrimp_Roll)
            markup1.add(item_Kitchen)
            bot.send_message(call.message.chat.id, 'Список булочек ->', reply_markup=markup01)
            bot.send_message(call.message.chat.id, 'Список булочек ->', reply_markup=markup02)
            bot.send_message(call.message.chat.id, 'Список булочек ->', reply_markup=markup03)
            bot.send_message(call.message.chat.id, 'Список булочек ->', reply_markup=markup04)
            bot.send_message(call.message.chat.id, 'Список Роллов ->', reply_markup=markup05)
            bot.send_message(call.message.chat.id, 'Назад ->', reply_markup=markup1)
        if call.data == 'Obed_Cheese':
            print(f"cheese{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Чизбургера')
            Photo_01 = open('./obed_png/Cheese_01.png', 'rb')
            Photo_02 = open('./obed_png/Cheese_02.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_photo(call.message.chat.id, Photo_02)

            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)


        if call.data == "Obed_Hamburger":
            print(f"hamburger{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Гамбургер')
            Hamburger_Photo_01 = open('./obed_png/Hamburger_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Hamburger_Photo_01)
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        if call.data == "Obed_Burger":
            print(f"burger{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Бургера')
            Burger_Photo_01 = open('./obed_png/Burger_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Burger_Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Double_Cheese":
            print(f"cheese{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Двойного Чизбургера')
            Double_Cheese_Photo_01 = open('./obed_png/Double_Cheese_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Double_Cheese_Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Grand":
            print(f"grand{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Гранд Чизбургера')
            Grand_Cheese_Photo_01 = open('./obed_png/Grand_Cheese_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Grand_Cheese_Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Grand_Deluxe":
            print(f"deluxe{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Гранд Делюкс Чизбургера')
            Photo_01 = open('./obed_png/Grand_Deluxe_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Double_Grand":
            print(f"double_grand{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Двойного Гранд Чизбургера')
            Photo_01 = open('./obed_png/Double_Grand_Cheese_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_FishBurger":
            print(f"obed_fishburger{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт ФишБургера')
            Photo_01 = open('./obed_png/FishBurger(01).png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Double_FishBurger":
            print(f"double_fishburger{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Двойного ФишБургера')
            Photo_01 = open('./obed_png/Double_FishBurger(01).png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        if call.data == "Obed_Cezar_Roll":
            print(f"cezar_roll{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Цезарь Ролла')
            Photo_01 = open('./obed_png/Cezar_Roll_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Shrimp_Roll":
            print(f"shrimp_roll{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Шримп Ролла')
            Photo_01 = open('./obed_png/Shrimp_Roll_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Speshl":
            print(f"speshl{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Биг Спешл')
            Photo_01 = open('./obed_png/Big_Speshl_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Double_Speshl":
            print(f"double_spleshl{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Двойного Биг Спешл')
            Photo_01 = open('./obed_png/Double_Big_Speshl_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Speshlx3":
            print(f"speshl_x3{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Биг Спешл три сыра(временно нету)')
            Photo_01 = open('./obed_png/Double_Big_Speshl_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Premier":
            print(f"{call.from_user.id} premier")
            bot.send_message(call.message.chat.id, 'Рецепт Премьер')
            Photo_01 = open('./obed_png/Premier_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Obed_Chiken_Hit":
            print(f"Chiken_Hit{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Рецепт Чикен Хит')
            Photo_01 = open('./obed_png/Chiken_Hit_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_obed = types.InlineKeyboardButton('Булочки Обед', callback_data='Bul_OB1') ## Булочки Обед
            markup.add(item_bulochki_obed)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        
        if call.data == "Friture_01":
            print(f"friture_Utro{call.from_user.id}")
            markup10 = types.InlineKeyboardMarkup(row_width=2)
            item_UHC_Timers = types.InlineKeyboardButton('UHC_Сроки Хранения', callback_data='UHC_Timer') ## Чизбургер
            markup10.add(item_UHC_Timers)
            bot.send_message(call.message.chat.id, 'Фритюр Утро', reply_markup=markup10)

        if call.data == "UHC_Timer":
            print(f"UHC_Timer{call.from_user.id}")
            Photo_01 = open('./zavtrak_png/UHC_Timer_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./zavtrak_png/UHC_Timer_02.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            item_Kitchen = types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Кухня кнопка
            markup1.add(item_Kitchen)
            bot.send_message(call.message.chat.id, 'Назад ->', reply_markup=markup1)
            
        
        if call.data == "Bul_BR2":
            print(f"Zavtrak_Menu{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Завтраки')
            markup05 = types.InlineKeyboardMarkup(row_width=2)
            item_Mafiins = types.InlineKeyboardButton('Булочки Маффины', callback_data='Zavtrak_Maffins') ## Чизбургер
            item_Tost= types.InlineKeyboardButton('Тосты', callback_data="Zavtrak_Tosti") ## Гамбургер
            item_Zavtraki = types.InlineKeyboardButton('Рецептура завтраков', callback_data='Zavtrak_Zavtraki') ## 
            item_Double_Cheese = types.InlineKeyboardButton('Двойной \n Чизбургер', callback_data='Obed_Double_Cheese') ## 
            markup05.add(item_Mafiins,item_Tost,item_Zavtraki)
            bot.send_message(call.message.chat.id, 'Список булочек ->', reply_markup=markup05)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            item_Kitchen = types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Кухня кнопка
            markup1.add(item_Kitchen)
            bot.send_message(call.message.chat.id, 'Назад ->', reply_markup=markup1)
                        
        
        if call.data == "Zavtrak_Maffins":
            print(f"Zavtrak_Maffins{call.from_user.id}")
            Photo_01 = open('./zavtrak_png/maffins_01.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id, "Булочки Маффин состоят из двух частей. \n Верхушка — это верхняя часть булочки. \n Пенек — это нижняя часть булочки.")
            bot.send_message(call.message.chat.id, "Перед использованием булочки должны быть разморожены до комнатной температуры. Нельзя использовать замороженный продукт.")
            Photo_01 = open('./zavtrak_png/maffins_02.jpg', 'rb')   
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id, "1 | Расчет партии. \n Опираясь на данные E-Production и запасы в UHC (ориентируйтесь на пустые лотки для булочек), решите, сколько булочек нужно приготовить. ")
            bot.send_message(call.message.chat.id, "2 | Подготовка. \n Откройте тостер для булочек, нажав на рычаг. Подготовьте лоток зелёного цвета c пластиковой вставкой с прорезями ")
            bot.send_message(call.message.chat.id, "3 | Разделение. \n Разделите булочки, держа их двумя руками и взяв большими пальцами за срез. Избегайте круговых движений, чтобы не сломать булочку. ")
            bot.send_message(call.message.chat.id, "4 | Раскладка. \n Разложите булочки на лопатке срезом вверх: верхушки ближе к ручке, пеньки –дальше. Не готовьте больше 5 булочек в одной партии. ")
            bot.send_message(call.message.chat.id, "5 | Закладка. \n Поместите лопатку с булочками в тостер для Маффинов и закройте дверцу, потянув на себя левую ручку. Таймер включится автоматически. Для 1–3 булочек —включите таймер половинной закладки. Для 4–5 булочек —просто закройте дверцу. ")
            bot.send_message(call.message.chat.id, "6 | Достаньте. \n Когда раздастся сигнал таймера, откройте дверцу тостера, нажав на левую ручку, и достаньте булочки. Положите пеньки срезом вверх в зелёный глубокий лоток UHC с прорезями с пластиковой вставкой. Затем положите верхушки сверху на пеньки, срезом вверх. Не кладите в лоток больше 5 булочек.")
            bot.send_message(call.message.chat.id, "7 | Перемещениев UHC. \n Немедленно поместите лоток в ячейку для булочек в UHC и включите таймер. Срок хранения готовых булочек Маффин — 15 минут. ")
            bot.send_message(call.message.chat.id, "8 | Очистка. \n Очистите рабочую поверхность тостера и удалите загрязнения.")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_breakfest= types.InlineKeyboardButton('Булочки Завтрак', callback_data='Bul_BR2') ## Булочки Завтрак
            markup.add(item_bulochki_breakfest)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
            
        if call.data == "Zavtrak_Tosti":
            print(f"Zavtrak_Tosti{call.from_user.id}")
            Photo_01 = open('./zavtrak_png/Tost_01.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id, "Ингредиенты для Тостов. \n Стандартные булочки.\n Сыр Чеддер \n Ветчина")
            bot.send_message(call.message.chat.id, "1 Расчет партии. | \n Опираясь на данные E-Production и запасы в UHC, решите, сколько тостов нужно приготовить.")
            bot.send_message(call.message.chat.id, "2 Подготовка. | \n Проверьте наличие лотков UHC чёрного цвета с металлической вставкой для Тостов с сыром и мелких лотков серого цвета с металлической вставкой для Тостов с ветчиной.")
            bot.send_message(call.message.chat.id, "3 Разложите. \n Положите лист тостерной бумаги на лопатку для булочек. Положите на лопатку ближе к ручке необходимое количество стандартных булочек (не более 6 штук) верхушками вверх. Отделите верхушки и разместите их срезом вниз на передней части лопатки. ")
            bot.send_message(call.message.chat.id, "4 Размещение продукта. | \n Положите 2 кусочка сыра, расположив их «звёздочкой», на каждую верхушку для Тоста с сыром. Положите по 1 ломтику круглой ветчины между ломтиками сыра для Тоста с ветчиной. Накройте заправленные верхушки пеньками, расположив их срезом вверх. Накройте подготовленные булочки сверху листом тостерной бумаги.")
            bot.send_message(call.message.chat.id, "5 Загрузите. \n Вставьте специальный зажим с ручкой между нижней и средней пластинами тостера. Поместите лопатку с булочками на среднюю пластину тостера. Выньте лопатку, оставив булочки в тостере, заключённые между листами тостерной бумаги. Закройте тостер.  ")
            bot.send_message(call.message.chat.id, "6 Сбор продукта. \n По сигналу таймера откройте тостер и выньте Тосты вместе с тостерной бумагой с помощью лопатки. Поместите Тосты на металлический поднос на заправочном столе. Аккуратно отделите листы бумаги от Тостов. ")
            bot.send_message(call.message.chat.id, "7 Перемещение в UHC. | \n Поместите Тосты с сыром в лоток UHC чёрного цвета с металлической вставкой, Тосты с ветчиной – в мелкий лоток серого цвета с металлической вставкой. Кладите в лоток не более 4 Тостов. Поместите лоток с Тостами в UHC и включите таймер на 20 минут")
            bot.send_message(call.message.chat.id, "8 Очистка. | \n Очистите рабочую поверхность тостера и удалите загрязнения  ")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_breakfest= types.InlineKeyboardButton('Булочки Завтрак', callback_data='Bul_BR2') ## Булочки Завтрак
            markup.add(item_bulochki_breakfest)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "Zavtrak_Zavtraki":
            print(f"Zavtrak_recept{call.from_user.id}")
            Photo_01 = open('./zavtrak_png/Recept_Zavtraki_00.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            
            Photo_01 = open('./zavtrak_png/Recept_Zavtraki_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_bulochki_breakfest= types.InlineKeyboardButton('Булочки Завтрак', callback_data='Bul_BR2') ## Булочки Завтрак
            markup.add(item_bulochki_breakfest)
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        
        if call.data == "Grille_02":
            print(f"Grille_02{call.from_user.id}")
            Photo_01 = open('./grillie_obed/grillie_01.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grillie_obed/grillie_02.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grillie_obed/grillie_03.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grillie_obed/grillie_04.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01) 
            video = open("./grillie_obed/grillie_video_01.MOV", "rb")
            bot.send_video(call.message.chat.id, video)
            video = open("./grillie_obed/grillie_video_02.MP4", "rb")
            bot.send_video(call.message.chat.id, video)
            Photo_01 = open('./grillie_obed/grillie_05.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01) 
            time.sleep(5)
            Photo_01 = open('./grillie_obed/grillie_06.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01) 
            time.sleep(5)
            Photo_01 = open('./grillie_obed/grillie_07.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            time.sleep(5)
            Photo_01 = open('./grillie_obed/grillie_08.jpg', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_Kitchen= types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Булочки Завтрак
            markup.add(item_Kitchen) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        if call.data == "C":
            print(f"C{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'в разработке', ) 
        if call.data == "hospitality":
            print(f"hospitality{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'в разработке(недостаточно информации о модулях)', )
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_hospitality_vas = types.InlineKeyboardButton('Всё начинается с вас', callback_data='hospitality_vas') ## Obhod
            item_hospitality_guest = types.InlineKeyboardButton('формирование\n впечатления\n гостей', callback_data='hospitality_guest') ## Obhod
            item_hospitality_01= types.InlineKeyboardButton('Создание \nвосхительных\n моментов\n хорошего\n настроения', callback_data='hospitality_obzor') ## Obhod
            markup.add(item_hospitality_01,item_hospitality_vas,item_hospitality_guest) 
            bot.send_message(call.message.chat.id, 'Модули:', reply_markup=markup)
            bot.send_message(call.message.chat.id, "Назад /commands", )
        

        if call.data == "hospitality_obzor":
            print(f"Hospitality_obzor{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Что такое гостеприимство?\nГостеприимство — это радушные приветствия, теплые прощания, улыбки и визуальный контакт. \nНаши принципы гостеприимства не предполагают широких жестов. Это простые, но важные мелочи, которые помогают дарить нашим гостям восхитительные моменты хорошего настроения: \nдружеское приветствие человеку, переступающему порог, или предложение помочь донести поднос;  \nкороткая беседа о том, как складывается день, или помощь в оформлении заказа через киоск самообслуживания.\nГостеприимство помогает нам создать гостям моменты хорошего настроения, и мы все принимаем в этом участие.\nДавайте узнаем, как выглядит гостеприимство, посмотрев следующее короткое видео (будет доступно позже)\n', )
            bot.send_message(call.message.chat.id, 'Создание восхитительных моментов хорошего настроения\nУ наших гостей есть определенные ожидания, которые мы должны уважать. Они надеются каждый раз получать качественные блюда,\nпричем именно те, что заказывали.  Они ждут особого подхода, который выделяет нас на фоне других подобных заведений. Наконец,\nони рассчитывают, что их заказ будет приготовлен быстро.\nМы нашли новый способ, который позволяет нам всегда создавать гостям восхитительные моменты хорошего настроения. Он звучит так:' )
            bot.send_message(call.message.chat.id, 'Наше кредо — выполнять обещания\nМы считаем, что дали нашим гостям обещание. Поэтому каждое наше действие и методы общения с гостями и коллегами\nподчиняются трем основным принципам:\n1.Делать правильно(Мы уделяем внимание даже самым незначительным мелочам.)\n2.Делать особенным(Мы делаем все возможное, чтобы у гостей остались наилучшие впечатления. Мы не просто оправдываем ожидания: мы стремимся их превзойти.)\n3.Делать быстро(Мы всегда исполняем свои обещания: обслуживаем гостей быстро и заботимся об их комфорте.)\nВаша задача — создавать хорошее настроение\nУ наших гостей есть определенные ожидания, которые мы пообещали удовлетворить. Как мы можем сдержать это обещание?\nПосмотрите следующее короткое видео (будет доступно позже).', )
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_hospitality= types.InlineKeyboardButton('Гостепреимство', callback_data='hospitality') ## Obhod
            markup.add(item_hospitality) 
            bot.send_message(call.message.chat.id, 'Назад', reply_markup=markup)
        if call.data == "hospitality_vas":
            print(f"Hospitality_vas{call.from_user.id}")
            
            bot.send_message(call.message.chat.id,"Все начинается с вас\nКачественное обслуживание начинается с вас. Оно зависит от того, о чем вы думаете, как себя чувствуете и как выглядите каждый день.\nВ этом разделе мы будем рассматривать первый комплекс умений, который лежит в основе качественного обслуживания гостей. Эти модели поведения необходимо оттачивать при общении с каждым гостем.\n*Первое впечатление\n*Вежливость\n*Образ мышления\n*Теплота и приветливость\nКогда вы больше узнаете о нашем предприятии, вы сможете разработать собственные модели поведения, позволяющие показать гостю особое отношение (видео будет доступно позже).")
            bot.send_message(call.message.chat.id,"Прекрасные первые впечатления\nКогда гость входит в зал, он делает мгновенный мысленный «снимок», запечатлевая вас и то, что вас окружает. Таким образом он неосознанно формирует свое первое впечатление. Если оно хорошее, гость настраивается на приятное времяпрепровождение в окружении дружелюбного персонала, всегда готового помочь. Иными словами, у гостя формируется настрой. \n1.Внешний вид(Ваш внешний вид имеет большое значение. Насколько чистой и аккуратной выглядит ваша униформа?)\n2.Язык тела(Невербальные сигналы могут рассказать гостям о вашем настроении и даже о том, насколько вы готовы им помочь.)\n3.Окружающая обстановка(Важен не только ваш внешний вид, но и то, что вас окружает. Возможно, рядом стоит переполненное мусорное ведро? Может, прилавок, за которым вы работаете, заляпан кетчупом?)")
            bot.send_message(call.message.chat.id,"Вежливость\nГости ценят вежливое отношение. Ваши слова, фразы и поведение несут в себе мощный посыл. Они показывают гостям, насколько вы заботитесь о них.\nИспользуйте в разговоре вежливые фразы, например: Спасибо,Пожалуйста,Извините, Чем я могу вам помочь?\n Быть вежливым нетрудно, но об этом легко забыть в суматошном ритме при наплыве гостей.  Поэтому всегда помните: вежливость не требует усилий, но может сильно повлиять на гостей и их впечатления.")
            bot.send_message(call.message.chat.id,"Образ мышления\nСтремитесь проявлять свои лучшие качества и всегда ищите возможности стать еще лучше. Заражайте других радостью и хорошим настроением.\nЭто не всегда легко, но если вы постараетесь, то у вас все получится. Гости заметят вас, откликнутся на ваш позитивный настрой и проникнутся к вам уважением. Вы сможете работать эффективнее и находить удовольствие во всем, что бы вы ни делали.\nЛишь один человек несет ответственность за вас, и это — вы сами. Стремитесь постоянно улучшать себя и добивайтесь новых успехов!\nЛюди чутко реагируют на эмоции окружающих и могут легко «копировать» чужое настроение. \nЛюди чутко реагируют на эмоции окружающих и могут легко «копировать» чужое настроение.")
            bot.send_message(call.message.chat.id,"Упражнение на размышление\nЗапомните: то, как вы мыслите, влияет на ваше поведение, а значит, и на впечатления гостей. \nНайдите время поразмыслить над приведенными ниже вопросам:. \nЧто больше или чаще всего портит вам настроение?\nКто еще страдает от вашего плохого настроения? \nЧто в такой ситуации вы можете сделать, чтобы изменить свое настроение?\nЧто вы делаете, чтобы домашние дела не влияли на ваше настроение на работе?\nС кем вы можете поговорить, если у вас не получается поднять себе настроение?")
            bot.send_message(call.message.chat.id,"Как поднять настроение себе и другим\nНастроением совершенно осознанно и успешно можно управлять. Мы начнем с самого простого. Самая простая техника – фокус на позитиве. \nПредлагаем тебе освоить несколько техник - ответь на простые вопросы.\nЧто хорошего происходит со мной прямо сейчас? – Важно перечислить минимум 10 вещей, пусть даже самых простых. Например, нахожусь в тёплом помещении.\nЧто хорошего я встретил(а) сегодня, пока шел на работу – перечислите минимум 10 вещей\nЧто хорошее у меня есть в планах, что я ожидаю – перечислите минимум 10 вещей\nКомплименты коллегам. Например: «Ты очень позитивный, мне приятно с тобой работать!»\n")
            bot.send_message(call.message.chat.id,"Теплота и приветливость\nИзвестно ли вам, что то, как вы говорите, важнее того, что вы говорите? А еще важнее невербальные сигналы. Каким в вашем представлении должно быть теплое и приветливое обслуживание? \nИмейте в виду, что гости сразу почувствуют вашу неискренность. Следите, чтобы между вашими словами и мимикой не возникало расхождений.\n")
            bot.send_message(call.message.chat.id,"Радушный прием гостей\nИзвестно ли вам, что гостеприимство начинается с вас: от ваших мыслей и ощущений зависит, насколько радушный прием вы сможете оказать. Приветствуя гостей, вы получаете возможность создать у них хорошее первое впечатление и дать почувствовать, что вы им искренне рады. От того, как вы встретите гостей, зависит, понравится ли им этот опыт посещения (видео будет доступно позже). \n")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_hospitality= types.InlineKeyboardButton('Гостепреимство', callback_data='hospitality') ## Obhod
            markup.add(item_hospitality) 
            bot.send_message(call.message.chat.id, 'Назад', reply_markup=markup)
            
        if call.data == "hospitality_guest":
            print(f"Hospitality_guest{call.from_user.id}")
            bot.send_message(call.message.chat.id,"Цикл обслуживания гостей\nКаждый наш гость проходит определенный цикл обслуживания. Цикл обслуживания представляет собой маршрут, по которому двигается гость, выбравший наши предприятия. Он состоит из пяти ключевых этапов — и каждый из них может либо порадовать гостей, либо испортить им впечатление от посещения. Пять ключевых этапов цикла обслуживания:")
            Photo_01 = open("./hospitality/hospitality_01.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Решающие моменты\nРешающие моменты — это ключевые пункты, которые позволяют понять, соответствуем ли мы ожиданиям гостей. Теперь, когда мы знаем, чего ждет гость, давайте посмотрим, как оправдать его ожидания.\nВзгляните на наших гостей и послушайте, что они говорят о нашем обслуживании и о том, что стало для них решающим моментом (видео будет доступно позже). ")
            bot.send_message(call.message.chat.id,"Ваша роль в цикле обслуживания гостей\nВы получили представление о цикле обслуживания гостей и о решающих моментах. Теперь вы узнаете, как взаимосвязаны эти понятия и как использовать ваши знания, чтобы реализовать на практике принцип \n«Делать правильно, делать особенным и делать быстро».\n1.Делать правильно (Мы уделяем внимание даже самым незначительным мелочам.)\n2.Делать особенным(Мы делаем все возможное, чтобы у гостей остались наилучшие впечатления. Мы не просто оправдываем ожидания: мы стремимся их превзойти.)\n3.Делать быстро (Мы всегда исполняем свои обещания: обслуживаем гостей быстро и заботимся об их комфорте.)\nЭто важнейшее условие, позволяющее создавать моменты хорошего настроения нашим гостям. \nДети любят приходить в наши ПБО, но помните, что все изменилось, и мы не можем подойти к ним слишком близко: \nОбъясняйте семьям, куда идти и соблюдайте социальное дистанцирование. Поощряйте бесконтактные способы оплаты. \nНе раздавайте воздушные шарики и не выдавайте цветные карандаши детям, а также другие сувениры. ")
            bot.send_message(call.message.chat.id,"Ожидания гостей\nКаждый день мы обслуживаем миллионы гостей, и у каждого из них свои желания и потребности. Чтобы создавать моменты хорошего настроения, важно понимать гостей и знать, что они ждут от визита к нам.\nМы видим в каждом посетителе не просто клиента, а гостя.  \nДавайте узнаем, как дарить незабываемые впечатления нашим гостям (видео будет доступно позже). \nЗадача по тренировке гостеприимства.\nСимпатия с первого взгляда.\nНавыки гостеприимства нужно развивать. Возможно, вам потребуется время, чтобы научиться свободно общаться с гостями.\nДля начала научитесь приветствовать гостей раньше, чем они сделают это сами.\nВы должны всегда первым говорить «здравствуйте», «до свидания» и «спасибо».")
            bot.send_message(call.message.chat.id,"Встреча гостей\nК нам приходят разные гости. Условно мы их разделили на 4 категории, которые чаще всего вы можете встретить в наших предприятиях:\nсемьи с детьми\nстуденты\nофисные сотрудники\nпожилые люди\nВсе они приходят в наши ПБО по разным причинам, и поэтому к ним нужен разный подход.  Вам предстоит научиться подстраиваться под потребности конкретного гостя.\n")
            bot.send_message(call.message.chat.id,"Поставьте себя на место гостя\nЭто упражнение выполняется вместе с инструктором. \nРассмотрите цикл обслуживания и решающие моменты глазами наших разных гостей: Джерома, Эммы, Кэндис и Тодда. В этом упражнении вам надо поставить себя на место гостя и поразмыслить о том, чего он хочет и ради чего пришел к нам. \nЭтап 1\nВыберите одного из гостей и посмотрите, чего он ждет от своего визита.")
            Photo_01 = open("./hospitality/hospitality_02.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./hospitality/hospitality_03.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Этап 2\nВыйдите на улицу. Закройте глаза и представьте, что вы и есть тот гость, которого вы выбрали. \nОткройте глаза и пройдите поэтапно весь цикл обслуживания, наблюдая за происходящим глазами гостя. \n")
            Photo_01 = open("./hospitality/hospitality_01.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"На каждом этапе обслуживания отвечайте на приведенные ниже вопросы.\nЧто вы видите?\nЧто вы слышите? \nЧто вы чувствуете?\nПомните, что вы и есть выбранный вами гость. Чтобы ответить на эти вопросы, вам нужно мыслить нестандартно. Отлично! Подойдите к заданию творчески и постарайтесь понять, что значит — быть этим гостем.\nКакие возможности вы заметили? Подумайте о том, как реализовать принцип «Выполнять обещания» и обеспечить нашим гостям особое отношение и быстрое, качественное обслуживание\nК нам приходят разные гости, могут прийти и люди с различными видами инвалидности. Как создавать для них моменты хорошего настроения, можно ознакомиться в модуле Взаимодействие с людьми с ограниченными возможностями здоровья.\n ")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_hospitality= types.InlineKeyboardButton('Гостепреимство', callback_data='hospitality') ## Obhod
            markup.add(item_hospitality) 
            bot.send_message(call.message.chat.id, 'Назад', reply_markup=markup)

        if call.data == "DLK":
            print(f"DLK{call.from_user.id}")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_Guest= types.InlineKeyboardButton('Гость', callback_data='DLK_Guest') ## Guest
            item_Obzor= types.InlineKeyboardButton('Обзор', callback_data='DLK_Obzor') ## Obzor
            item_Timer= types.InlineKeyboardButton('Сроки Хранения', callback_data='DLK_Timer') ## Timers
            item_Obhod= types.InlineKeyboardButton('Обход', callback_data='DLK_Obhod') ## Obhod
            item_Truck= types.InlineKeyboardButton('Разгрузка Машины', callback_data='DLK_Truck') ## Obhod
            markup.add(item_Guest,item_Obzor,item_Timer,item_Obhod,item_Truck) 
            bot.send_message(call.message.chat.id, 'DLK', reply_markup=markup)
            bot.send_message(call.message.chat.id, "Назад /commands", )
        if call.data == "DLK_Truck":
            print(f"DLK_Truck{call.from_user.id}")
            bot.send_message(call.message.chat.id,"Разгрузка Машины \n Прием машины\nНа вашем предприятии может использоваться один из вариантов доставки продуктов из Распределительного Центра.\nОбычная – выгрузка с участием сотрудников ПБО и поддержке водителя, пересчет и заполнение документов\nДоверительная - выгрузка с участием сотрудников ПБО и поддержке водителя, без пересчета и заполнения документов\nНевидимая (небольшое число ПБО) - выгрузка без сотрудников ПБО, пересчета, расстановка в ПБО\nУточните у инструктора, какой вид доставки используется в вашем ПБО.\nПродукты, упаковка и полуфабрикаты доставляются на наши предприятия компанией HAVI (видео будет доступно позже).\nКо времени прихода машины с продукцией работники ПБО обеспечивают свободный доступ машины к зоне парковки и разгрузки (видео будет доступно позже).\nИзучите следующие процедуры, если на вашем предприятии применяются обычная или доверительная доставка\nКак только двери кузова открываются, происходит теплообмен. Поэтому, при выгрузке «температурной» продукции, необходимо стремиться осуществить эту операцию\nв максимально короткий срок и предотвратить размораживание продукции (видео будет доступно позже).\nПри приеме в ПБО замороженных булочек, их необходимо сразу завозить во фризер. Максимально время нахождения булочек вне фризера - 15 мин (видео будет доступно позже).\nПри разгрузке машины, выполняйте все инструкции от вашего менеджера (видео будет доступно позже).")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_DLK = types.InlineKeyboardButton('Доcтавка Модули', callback_data='DLK') ## Доставка Кнопка
            markup.add(item_DLK) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        if call.data == "DLK_Obzor":
            print(f"DLK_Obzor{call.from_user.id}")
            bot.send_message(call.message.chat.id,"Обзор")
            Photo_01 = open("./DLK/DLK_06.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_07.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Как предотвратить поскальзывания, спотыкания и падения \n Ниже описаны меры предотвращения поскальзывания, спотыкания и падения.\n Поддерживайте полы в чистоте.\n Сразу же вытирайте разлитое или рассыпанное.\n Устраняйте небольшие загрязнения при помощи продезинфицированных тряпочек или бумажных полотенец.\nУстанавливайте предупреждающие знаки «Осторожно, мокрый пол».\nВытирайте полы насухо сразу после влажной уборки.\nНосите подходящую обувь на нескользящей подошве и низком устойчивом каблуке.")
            Photo_01 = open("./DLK/DLK_08.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Мусорная комната (компакторная) \n Мусорная комната. Дверь в мусорную комнату должна быть всегда закрыта на замок. \nЕсли приехала машина, чтобы забрать мусор, то рядом с открытой дверью всегда должен находиться менеджер. Проверяйте, чтобы после отгрузки мусора дверь была закрыта на замок.\n В мусорных мешках бывают легковоспламеняющиеся вещества, поэтому в мусорной комнате нельзя курить, как и в других помещениях.\nНе используйте дверь в мусорную комнату для входа в здание и выхода из него, даже если вы видите, что дверь открыта. В этом случае обязательно позовите менеджера.")
            Photo_01 = open("./DLK/DLK_09.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Работа на высоте\nРаботой на высоте считается любая работа, при которой ноги не касаются пола. \n Например, когда вы поднимаетесь по стремянке, чтобы достать что-то с верхней полки на складе или протереть окно, до которого не дотягиваетесь, вы работаете на высоте. \n Давайте посмотрим, что нужно принять во внимание, работая на высоте:\n  1.Проверьте, не сломана ли стремянка \n 2.Убедитесь, что ее ступеньки исправные, чистые и сухие. \n 3.Проверьте наличие всех четырех нескользящих наконечников на ножках. \n 4.Устойчиво поставьте стремянку на ровную поверхность. \n 5.Ее ножки должны находиться в самом широком положении, а боковины должны быть зафиксированы.\n 6.Стойте посредине и не наклоняйтесь в стороны. \n 7.Не поднимайтесь на две верхние ступени. \n 8.Не пытайтесь дотянуться до чего-либо со стремянки. \n ПОЧЕМУ?  Зная, как предотвращать поскальзывания, спотыкания и падения и какие меры можно предпринять, вы повышаете не только свою безопасность, но и безопасность коллег.")
            Photo_01 = open("./DLK/DLK_10.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"И дома, и на работе мы каждый день поднимаем и носим тяжелые предметы. Чтобы не причинить вред здоровью, важно соблюдать некоторые правила. \nНиже описано, как правильно поднимать тяжелое. \n 1.Убедитесь, что держите груз крепко. \n 2.Согните ноги в коленях, держите спину прямо и поднимайте груз при помощи мышц ног.\n 3.Держите груз как можно ближе к телу. \n4.Выпрямите руки, но не блокируйте локтевые суставы.\n 5.Расставьте ноги, выставив одну из них немного вперед. \n6.Убедитесь, что вам хорошо видно, куда вы идете.\n7.Держите спину прямо, когда поднимаете, несете и опускаете груз. Не поворачивайте туловище. \n8.Если груз слишком тяжелый, не пытайтесь перемещать его самостоятельно, а обратитесь за помощью. \n ПОЧЕМУ? Если поднимать тяжести неправильно, можно навредить себе, даже если вы уверены, что справитесь с этим весом. Соблюдая технику безопасности, вы снижаете риск травмы. ")
            bot.send_message(call.message.chat.id,"Знакомство с оборудованием, используемым при работе в доставке \n режде чем приступить к работе на смене, вы должны получить представление об оборудовании и инструментах, с которыми будете работать.")
            Photo_01 = open("./DLK/DLK_11.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Установка полиэтиленового пакета \n 1.Нажмите кнопку на нижней подставке и удерживайте, как минимум, две секунды.\n2.Нажмите ножную педаль.\n3.Нажмите рычажный клапан сверху, канистра начнет движение вверх.\n4.Наденьте на канистру полиэтиленовый пакет.\n5.Нажмите на кнопку снизу - канистра начнет движение вниз.\n6.Остановите канистру, нажав на ножную педаль.\n7.Отодвиньте пресс назад - оборудование готово к использованию")
            bot.send_message(call.message.chat.id,"Прессование \n 1.Поместите отходы в канистру.\n2.Верните пресс в исходное положение.\n3.Нажмите рычажный клапан сверху для автоматического цикла прессования.\nСнятие полиэтиленового пакета с мусором \n1.Нажмите кнопку на нижней подставке и удерживайте, как минимум, две секунды.\n2.Нажмите ножную педаль.\n 3.Нажмите рычажный клапан сверху, канистра начнет движение вверх.\n4.Завяжите полиэтиленовый пакет и снимите его с подставки, установите новый пакет.")
            Photo_01 = open("./DLK/DLK_12.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"1.Гидравлические тележки должны перемещаться рабочими, находящимися впереди нее.\n 2.Перед использованием необходимо проверить исправность гидравлических тележек.\n3.Запрещается: нагружать тележки свыше их максимальной грузоподъемности, садиться и кататься на тележках, применять рабочий инвентарь не по назначению.\n4.Размещайте груз на грузонесущую платформу и тележки в горизонтальной плоскости, исключайте возможность падения груза или опрокидывания тележки.\n5. После использования уберите тележку в специально отведенное место, установите ее на ровную поверхность, рама тележки должна быть опущена в нижнее положение.")
            Photo_01 = open("./DLK/DLK_13.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_14.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"CO2 хранится в жидком состоянии в баллонах низкого или высокого давления.  \n СО2 используется в ПБО для газирования напитков и для перемещения других жидкостей, таких, как сиропы, чай и кетчуп в точки использования.")
            bot.send_message(call.message.chat.id,"Правила при транспортировке баллонов\n1.Во время погрузки и разгрузки автомашины выключить ее двигатель.\n2.При отсутствии грузоподъемных механизмов погрузо-разгрузочные работы следует производить не менее чем двум работникам.\n3.Баллоны следует разгружать башмаками вниз.\n4.Производить транспортировку баллонов только с навинченными на их горловины предохранительными колпаками и заглушками.\n5.Не допускать падения и повреждения баллонов, предохранять баллоны от солнечных лучей.\n6.Не допускается переноска баллонов на руках и плечах.\n7.Транспортировать баллоны на специальных тележках, оборудованных ложементами и имеющих хомуты крепления баллонов или оснащенных упорами (скобами), предотвращающими смещение или падение баллонов.\n8.На небольшое расстояние газовые баллоны допускается перемещать методом кантования (перекатывания на ребре башмака).")
            Photo_01 = open("./DLK/DLK_16.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_DLK = types.InlineKeyboardButton('Доcтавка Модули', callback_data='DLK') ## Доставка Кнопка
            markup.add(item_DLK) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)
        if call.data == "DLK_Obhod":
            print(f"DLK_Obhod{call.from_user.id}")
            bot.send_message(call.message.chat.id,"Процедуры открытия:\nВынести продукцию\nВ первую очередь необходимо вынести на кухню и прилавок продукцию, оставшуюся после закрытия предприятия. Перед выносом на кухню, нужно переложите булочки из транспортной тары в лотки красного цвета.\nПринять смену\nУзнайте информацию от менеджера смены, проверьте задания из графика регламентных работ на стенде доставки.\nПроверить сроки хранения\nПроверьте даты реализации и соблюдение вторичных сроков хранения продуктов и полуфабрикатов.\nПроверить температуру\nПроверьте температуру в холодильных и морозильных камерах. При обнаружении несоответствия стандартным значениям сообщите менеджеру.\nОбеспечить запас продукции согласно принципу 24/2\nВажно обеспечить необходимый запас продукции и упаковки на кухне и прилавке в соответствии с принципом 24/2. Соблюдайте принцип ротации и требования по безопасности пищи. Заполните фризеры картофелем, филе, куриными продуктами, стартерами, пирогами в соответствии с Таблицами выдержки и приготовления и Таблицами запасов.\nПриготовьтесь к переходу\nУберите все замороженные полуфабрикаты Завтраков, уберите все продукты в холодильник. Уберите упаковку для Завтраков из зоны производства.\nСоблюдать правильное обращение с пустой тарой\nСвоевременно убирайте и складируйте пустую тару, в том числе и картонную упаковку в установленном месте.\n Запомните!!!Если вы заметили несоответствие веса или количества, температуры хранения, повреждение упаковки, продукцию с истекшим сроком хранения. Сообщите об этом менеджеру.")
            bot.send_message(call.message.chat.id,"Процедуры закрытия\n1.Перед закрытием предприятия своевременно оптимизируйте количество продуктов на производстве. Используйте Таблицы выдержки и приготовления и Таблицы запасов. \n2.Аккуратно упаковывайте продукцию, используя пищевую плёнку.\n3.После закрытия ПБО, убирайте всю продукцию с не истекшим сроком хранения.\n4.Все невскрытые упаковки (кейсы, сливсы) с продуктом, из зоны хранения на кухне, возвращайте в основной фризер/кулер/сухой сток.\n5.Уточните у менеджера, какая продукция должна быть списана, а какую необходимо убрать.")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_DLK = types.InlineKeyboardButton('Доcтавка Модули', callback_data='DLK') ## Доставка Кнопка
            markup.add(item_DLK) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)


        if call.data == "DLK_Timer":
            print(f"dlk_timer{call.from_user.id}")
            bot.send_message(call.message.chat.id,"Сроки хранения")
            Photo_01 = open("./DLK/DLK_17.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Запомните! \n Каждый раз, когда вы перемещаете продукт или меняете температуру его хранения, требуется проверять или менять показатель срока хранения.")
            bot.send_message(call.message.chat.id,"ПОЧЕМУ? Блюда, которые мы подаем гостям, влияют на их общие впечатления. Если им не понравится, они не вернутся к нам.")
            Photo_01 = open("./DLK/DLK_18.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"1.Поступающие в ПБО упаковка, полуфабрикаты и готовые продукты размещаются в соответствии с условиями хранения, которые рекомендует производитель к данной продукции.\n2.В первую очередь продукция размещается в соответствующие места хранения (морозильные и холодильные камеры, сухой склад). Хранение продукции осуществляется в транспортной упаковке.3.Для пополнения запасов на кухне продукты из основного кулера/фризера/сухого стока перемещаются до зоны кухни только в транспортной упаковке\n4.Для удаления транспортной пленки при входе в производственную зону используйте специальный стол/стеллаж для растаривания.\n5.Ротация продукции соответствует принципам FIFO. Партия с наименьшим сроком годности должна использоваться в первую очередь.\n6.Хранение на паллетах или стеллажах осуществляется с соблюдением расстояний:\n- Высота от пола - не менее 15 см;\n - Расстояние от стен - не менее 5 см;\n- Расстояние от испарителя - не менее 30 см в любом направлении;\n- Расстояние между колонами коробок - не менее 2,5 см;\n7.Соблюдение правил товарного соседства и внутренних стандартов предприятий нашей компании.")
            Photo_01 = open("./DLK/DLK_19.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_20.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_21.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_22.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_23.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_24.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_25.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Виды держателей и этикеток\nНа этикетке для любого вида держателя имеется:\nФотография продукта\nWRIN и название продукта\nКейсовость\nНеобходимое количество продукта при минимальном и максимальном товарообороте\nПоле для указания направления размещения продукта на стеллаже/паллете")
            Photo_01 = open("./DLK/DLK_26.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Эргономичное и эффективное хранение Экосима позволяет:\n1.Оптимизировать зоны хранения\n2.Снизить трудовые затраты при инвентаризации, приеме продукции и поиске необходимой продукции.\n3.Потенциально снизить отходы.\n4.Соблюдать правильную ротацию продуктов.\n5.Сократить количество изменений заказов и довозов.")
            Photo_01 = open("./DLK/DLK_27.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_28.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open("./DLK/DLK_29.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Таблицы выдержки и приготовления\nТаблицы выдержки помогают отслеживать, сколько и каких полуфабрикатов нужно выносить на разморозку/выдержку в зависимости от времени дня.")
            Photo_01 = open("./DLK/DLK_30.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Таблица запаса и выдержки полуфабрикатов содержит информацию о том, сколько полуфабрикатов нужно вынести из кулера (холодильника) в заданное время, чтобы\nони успели нагреться. Ниже описано, какие сведения содержатся в этой таблице.\n1.Название продукта. В этом столбце перечислены называния продуктов/ингредиентов, включенных в таблицу.\n2.Единица измерения.  В этом столбце указано, во что ингредиент упакован.\n3.Время выноса из кулера. В этом столбце указано, во сколько нужно достать продукт/ингредиент из кулера, чтобы он успел нагреться\n4.Выдержка. В этом столбце указано какое количество каждого вида продукта/ингредиента необходимо вынести в соответствующее время.")
            bot.send_message(call.message.chat.id,"Таблицы запасов\nС помощью таблиц запасов можно определить, какие объемы продуктов требуются на разных позициях, чтобы поддерживать спрос в определенное время дня. В эти\nтаблицы вносятся замороженные и охлажденные продукты, а также упаковка.\nТаблица дневного использования для сухого стока. Содержит данные о количестве упаковки и сопутствующих одноразовых продуктов, таких как трубочки, салфетки,\nложки. Ниже описано, какие сведения содержатся в этой таблице.\n1.Название продукта. В этом столбце перечислены названия наименований, включенных в таблицу.\n2.Использование. В этом столбце указано, каким должен быть уровень запасов на соответствующий период (будни или выходные).\n \n Таблица запасов с двухчасовым интервалом используется для отслеживания запасов замороженных продуктов, которые нужно пополнять в ходе смены. Здесь\nуказано, какой спрос ожидается каждые два часа, чтобы вы могли определить необходимый объем запасов. Ниже описано, какие сведения содержатся в этой таблице.\n1.Название продукта. В этом столбце перечислены называния полуфабрикатов, включенных в таблицу.\n2.Единица измерения. В этом столбце указано, во что  продукт упакован.\n3.Ожидаемая потребность в запасах с двухчасовым интервалом. В этом столбце указано, каким должен быть уровень запасов замороженного продукта в соответствующий двухчасовой период.")
            bot.send_message(call.message.chat.id,"Процедуры хранения и разморозки булочек\nВсе булочки, доставленные на предприятие, должны правильно храниться, размораживаться и аккуратно использоваться. Так же, как и мясные полуфабрикаты, они \nявляются одной из главных составляющих наших бургеров.\n")
            Photo_01 = open("./DLK/DLK_31.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Чтобы булочки соответствовали Золотому стандарту качества на всем пути до получения сандвича гостем, соблюдайте следующие процедуры:\n1.Сразу помещайте булочки в большой морозильник после доставки.\n2.Замороженные булочки храните только при температуре -18  -23 Co.\n3.Не допускайте перемещения булочек из большого морозильника в холодильник или коридор при пополнении запасов на этаже (например, для того чтобы достать из большого морозильника другие продукты) или во время разгрузки.\n4.Для размораживания размещайте булочки в помещении с комнатной температурой (точные условия на этикетке) с хорошей циркуляцией воздуха.\n5.Доставая булочки на разморозку, на каждый сливс устанавливайте таймер вторичного срока хранения. (Вторичный срок хранения булочек составляет 48 часов,включая 4 часа разморозки на стеллаже для булок и 10-12 часов в стопке).\n6.Булочки, доставленные в коробках, перекладываются для разморозки в булочные лотки. Нельзя размораживать булки в коробках.\n7.Для достижения оптимального качества булочек их необходимо доставать на разморозку из фризера не менее 2-х раз в день (в идеале 3 раза в день).\n8.Не допускается одновременная разморозка булочек в красных и коричневых лотках на стеллаже для булочек, т. к. это может привести к перекрёстному заражению.\n9.Приносите на кухню в первую очередь булочки с более ранним сроком окончания хранения")
            Photo_01 = open("./DLK/DLK_32.png", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Работа с тарой, тарирование лотков\nОборотной тарой, являются: евро и индустриальные поддоны, булочные лотки (коричневые и синие), баллоны СО2.\nРаботник ПБО складирует пустую тару в специально отведенном месте, для возврата ее на РЦ.\nПБО должен возвращать на РЦ всю тару без посторонних предметов, включая повреждённую (повреждённая тара списывается на РЦ).")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_DLK = types.InlineKeyboardButton('Доcтавка Модули', callback_data='DLK') ## Доставка Кнопка
            markup.add(item_DLK) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        if call.data == "DLK_Guest":
            print(f"DLK_Guest{call.from_user.id}")
            bot.send_message(call.message.chat.id,"Любовь к гостю")
            Photo_01 = open("./DLK/DLK_01.jpg", "rb")
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Чего ожидают гости от нашей продукции? \n Наши гости ожидают красивые, очень вкусные, горячие и свежие продукты. \n Чтобы достигать такого результата каждый день, нужно работать с прицелом на золотой стандарт качества продуктов и соблюдение сроков хранения полуфабрикатов. \n Превосходить ожидания наших гостей должно быть нашей главной задачей каждый рабочий день в любых обстоятельствах. Даже за мелкими и на первый взгляд незначительными процедурами есть твердое обоснование: мы им следуем, чтобы отвечать ожиданиям гостей. ")
            bot.send_message(call.message.chat.id,"Цикл обслуживания гостей")
            Photo_01 = open("./DLK/DLK_02.png", 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Ваши действия во время доставки продуктов очень важны, они влияют на скорость обслуживания гостей и качество обслуживания на всем пути цикла обслуживания гостей:")
            Photo_01 = open('./DLK/DLK_03.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Cпособы сдержать обещание")
            Photo_01 = open('./DLK/DLK_04.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./DLK/DLK_05.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_DLK = types.InlineKeyboardButton('Доcтавка Модули', callback_data='DLK') ## Доставка Кнопка
            
            markup.add(item_DLK) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)

        if call.data == "Grille_01":
            print(f"Grill_obed {call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Гриль обед:', )
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_safe = types.InlineKeyboardButton('Безопасность сотрудников', callback_data='Grill_Safe') ## Доставка Кнопка
            item_obzor = types.InlineKeyboardButton('Безопасность сотрудников', callback_data='Grill_obzor') ## Доставка Кнопка
            item_Kitchen = types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Кухня кнопка
            markup.add(item_safe,item_obzor,item_Kitchen) 
            bot.send_message(call.message.chat.id, "Модули:", reply_markup=markup)

        if call.data == "Grill_obzor":
            print(f"grill_obzor{call.from_user.id}")
             
            Photo_01 = open('./grille_obed(1)/grille_03.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grille_obed(1)/grille_04.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grille_obed(1)/grille_05.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grille_obed(1)/grille_06.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Процесс приготовления на гриле\nВам предстоит готовить на гриле разные мясные полуфабрикаты, но общий процесс работы с грилем примерно одинаков. ") 
            Photo_01 = open('./grille_obed(1)/grille_07.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grille_obed(1)/grille_08.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            video = open("./grille_obed(1)/grille_01.MP4", "rb")
            bot.send_video(call.message.chat.id, video)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_grille = types.InlineKeyboardButton('Назад', callback_data='Grille_01') ## Булочки Обед
            markup.add(item_grille) 
            bot.send_message(call.message.chat.id, "Назад", reply_markup=markup)

        if call.data == "Grill_Safe":
            print(f"grill_safe{call.from_user.id}")
            
            bot.send_message(call.message.chat.id,"Безопасность прежде всего\nПри работе на гриле необходимо заботиться о следующих двух аспектах: личная безопасность и безопасность пищи. Это касается каждого работника предприятия.\nДумайте о возможных последствиях для себя и своих товарищей по работе. Следите за безопасностью пищи (и наших гостей): берегите ее от химических загрязнений и\nпопадания посторонних предметов. Никому не захочется увидеть кусок пластмассы в своем сандвиче.")
            bot.send_message(call.message.chat.id,"Угроза личной безопасности\n1.На кухне может одновременно находиться много работников, поэтому старайтесь ни с кем не сталкиваться при перемещении и предупреждайте, куда вы идете.\n2.Во избежание несчастных случаев проверяйте свое оборудование и рабочий участок на предмет реальных или потенциальных рисков для безопасности. Не делайте ошибок, едва заступив на смену.\nВы работаете с оборудованием, которое сильно разогревается. Поверхности гриля представляют угрозу безопасности и способны обжечь все, что к ним прикасается. На гриле должны обжариваться продукты, а не ваши руки или лицо.")
            bot.send_message(call.message.chat.id,"Безопасность пищи: обработка\n1.Во избежание загрязнения мойте руки перед началом и после окончания работы на станции, когда работаете с сырыми продуктами, а также не реже одного раза в час.\n2.Работая на кухне, не снимайте перчатки. Чтобы предотвратить загрязнение, всегда используйте синие одноразовые перчатки при работе с сырыми продуктами на этой станции.\n3.Используйте специальные щипцы при снятии мяса с гриля . Это поможет избежать перекрестного заражения.")
            bot.send_message(call.message.chat.id,"Безопасность пищи: сроки, маркировка и униформа\n1.НЕ закладывайте продукты с просроченным сроком годности в морозильную камеру около гриля. Всегда проверяйте срок их годности! Проверяйте дату срока годности на упаковках с замороженными котлетами.\n2.Выбрасывайте продукты из UHC, если их таймер срока хранения истек. Кроме того, выбрасывайте продукты, которые не прошли надлежащую тепловую обработку или выглядят недостаточно хорошо.\n3.Строго соблюдайте правила внешнего вида, чтобы в пищу не попадали несъедобные предметы.")
            Photo_01 = open('./grille_obed(1)/grille_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            Photo_01 = open('./grille_obed(1)/grille_02.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"ДОПОЛНИТЕЛЬНЫЕ ПРОЦЕДУРЫ\n1.Правильное использование СИЗ (маски, перчатки, защитные экраны). \n2.Протирайте чистым продезинфицированным полотенцем все поверхности минимум каждый час, включая пин-пад, кассовые аппараты, прилавок и остальное оборудование. \n3.Мойте руки по мере загрязнения, но не реже одного раза в 60 минут. Продолжительность процесса мытья рук должна быть не менее 30 секунд (или процесс намыливания рук должен быть не менее 20 секунд).\n4.Обеспечивайте безопасное расстояние и соблюдайте социальное дистанцирование в 1,5 метра между гостями в зале, а также между сотрудниками.") 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_grille = types.InlineKeyboardButton('Назад', callback_data='Grille_01') ## Булочки Обед
            markup.add(item_grille) 
            bot.send_message(call.message.chat.id, "Назад", reply_markup=markup)

        if call.data == "Friture_02":
            print(f"friture_02{call.from_user.id}")
            bot.send_message(call.message.chat.id, 'Основные принципы', )
            bot.send_message(call.message.chat.id, 'На фритюрной станции приходится готовить много разных продуктов. \n Для их приготовления кухни предприятия оборудованы фритюрницами с несколькими ваннами. \n У нас есть кое-какие хитрости, которые помогают постоянно держать в запасе достаточное количество готовых, горячих и свежих продуктов. \n Они очень облегчают нам работу и помогают кормить гостей максимально вкусной едой.', )
            Photo_01 = open('./friture_02/friture_01.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id, 'Однако не стоит следовать руководству слишком буквально: если вы  часто списываете полуфабрикаты из за того, что закончился срок их хранения, скажите об этом менеджеру. \n Вполне вероятно, что необходимо изменить текущую таблицу. \n Вертикальная система производства: все полуфабрикаты в UHC  располагаются вертикально, чтобы было видно, сколько ячеек отведено каждому из них.  \n Благодаря вертикальной системе можно одним беглым взглядом проверять: \n в каких ячейках стоят лотки и работают таймеры, а значит, находятся готовые полуфабрикаты \n отображается ли на UHC оповещение, что у полуфабриката в соответствующей ячейке скоро истечет срок хранения, а значит, возможно, потребуется приготовление новой партии какие ячейки не используются\nДля того, что бы вовремя готовить достаточное количество полуфабрикатов, обращайте внимание на лотки, которые возвращаются к вам на фритюрную станцию. \n Цвет лотков показывает, какой продукт необходимо готовить.\nСейчас инструктор расскажет вам об этом подробнее.\nУзкие места: помните о «правиле трех». \n Если у вас  три или больше пустых лотков, позовите своих коллег, чтобы они помогли вам быстро пополнить запасы.' )
            Photo_01 = open('./friture_02/friture_02.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id, 'Приготовление куриных полуфабрикатов', )
            Photo_01 = open('./friture_02/friture_03.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id, '1.Примите решение: Посмотрите на лотки UHC на фритюрнице, проверьте  E-Production, и решите, какой полуфабрикат и в каком количестве нужно готовить. При необходимости возьмите дополнительный лоток. \n 2.Подготовьтесь: выберите нужную ванночку для приготовления - обращайте внимание на настройки на дисплее фритюрницы. \n 3.Загрузите: поставьте корзинку на поднос для сырых полуфабрикатов. \n Безопасность. Это предотвратит попадание панировки с сырых полуфабрикатов на готовый  продукт. \n Загрузите в корзинку нужное количество полуфабрикатов. \n 4.Приготовьте: аккуратно опустите корзинку с полуфабрикатом в соответствующую ванну так, чтобы не было брызг. Аккуратно встряхните корзинку в ванне или используйте щипцы, чтобы погрузить порции во фритюр, чтобы они были покрыты полностью. Нажмите кнопку старта. \n 5.Извлеките: когда время приготовления истечёт и сработает таймер, достаньте корзинку с готовым полуфабрикатом из ванны, дайте маслу стечь 5-10 секунд и переложите продукт в лоток UHC соответствующего цвета: Наггетсы - янтарный широкий, Чикенбургер - белый, Пикантная - чёрный, Куриные Крылья - жёлтый, Стрипсы - янтарный с жёлтой клипсой. Верните корзину на место. \n 6.Поставьте на хранение: поместите лоток с готовым полуфабрикатом в соответствующую ячейку UHC и запустите таймер.  \n Готовые куриные полуфабрикаты кладите в лоток UHC в один слой. Если они будут лежать друг на друге, то станут влажными, а также могут повредиться. \n 7.Следите за чистотой: после каждой партии удаляйте  с поверхности фритюра частички продукта, используя шумовку.', )
            bot.send_message(call.message.chat.id, 'Приготовление Рыбного полуфабриката', )
            bot.send_message(call.message.chat.id, 'Рыбный полуфабрикат жарится так же, как и куриные полуфабрикаты, но тут есть ряд важных моментов. Сейчас инструктор вам все расскажет и покажет. \n Готовьте рыбные полуфабрикаты в отдельной ванне. \n Используйте только синие лотки UHC и фритюрные корзины для доготовки рыбы, часто они бывают с синими ручками, чтобы не путать рыбу с курицей. \n Для сезонных рыбных полуфабрикатов могут использоваться лотки другого цвета. Например, креветки хранятся в UHC в янтарных лотках с синей клипсой.', )
            bot.send_message(call.message.chat.id, 'ПОЧЕМУ? Это поможет избежать смешения вкусов разных продуктов', ) 
            bot.send_message(call.message.chat.id,"Приготовление Сырных палочек")
            bot.send_message(call.message.chat.id,"Сырные палочки жарятся так же, как и куриные полуфабрикаты, но тут есть ряд важных моментов. Сейчас инструктор вам все расскажет и покажет.\n Готовьте Сырные палочки в отдельной ванне.\n Используйте e-Production, чтобы определить размер партии полуфабрикатов для доготовки. Загружайте в корзину ровно столько порций, сколько указано в таблице, но не более 1 сливса Сырных палочек. \n По сигналу таймера через 30 секунд встряхните корзину с Сырными палочками. Эта процедура предотвращает слипание и неравномерное обжаривание Сырных палочек при доготовке.\n Используйте только зелёные мелкие лотки UHC с металлической вставкой и фритюрные корзины без разделителя. Не используйте корзинки с разделителем, т.к. Сырные палочки будут застревать и повреждаться.")
            bot.send_message(call.message.chat.id,"ВАЖНО В лотке UHC можно хранить не более 1 сливса Сырных палочек, чтобы не повредить готовый продукт. Сырные палочки не должны лежать друг на друге\nПосле окончания срока хранения в UHC полуфабрикаты надо списать и выбросить в специальное мусорное ведро. \n Никогда не используйте полуфабрикат, если у него закончился срок хранения.")
            bot.send_message(call.message.chat.id,"Приготовление пирожков")
            Photo_01 = open('./friture_02/friture_04.png', 'rb')
            bot.send_photo(call.message.chat.id, Photo_01)
            bot.send_message(call.message.chat.id,"Пирожки жарятся так же, как и куриные полуфабрикаты, но порядок их приготовления предусматривает некоторые дополнительные действия и важные моменты. Сейчас инструктор покажет вам, как правильно жарить пирожки.\n Готовьте пирожки в отдельной ванне. \n Используйте поднос и специальное место для остывания пирожков.  Перед упаковкой охлаждайте пироги 20 минут.\n На каждую партию приготовленных пирожков установите таймер вторичного срока хранения  90 минут (время на остывание пирожков сюда входит).\n Кладите каждый пирожок в специальную коробку и клейте на язычок упаковки таймер вторичного срока хранения (90 минут от момента приготовления). \nУпакованные пироги с таймером кладите не в UHC, а в специальный шкаф для пирогов на прилавке. Соблюдайте принцип Первый пришёл - первый ушёл.  \nПОЧЕМУ? Отдельная ванна поможет избежать перекрестного заражения. А охлаждать пироги перед упаковкой нужно, чтобы гости не обжигались. ")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item_Kitchen= types.InlineKeyboardButton('Кухня', callback_data='Kitchen') ## Булочки Завтрак
            markup.add(item_Kitchen) 
            bot.send_message(call.message.chat.id, 'Назад -->', reply_markup=markup)


print(today)
print('bot_enable')
bot.polling(none_stop=True)
