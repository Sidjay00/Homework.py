# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""

import telebot
from telebot import types
import random

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, f"""\
Привет, {message.from_user.first_name}! Я бот Питоша.
Я загадал число от 1 до 1000, а ты попробуй его отгадать.
А когда отгадаешь, я скажу, с какой попытки у тебя это получилось.
Какое число я загадал?
""")
    number = random.randint(1, 1000)
    print(number)
    count = 1
    bot.register_next_step_handler(msg, process_is_digits, number, count)


def process_is_digits(message, number, count):
    try:
        print(message)
        user_number = message.text
        if not user_number.isdigit():
            msg = bot.reply_to(message, 'Вы указали не число.\nВведите число от 1 до 1000.')
            bot.register_next_step_handler(msg, process_is_digits, number, count)
            return
        elif int(user_number) > number:
            msg = bot.reply_to(message, 'Указанное вами число больше загаданного.')
            c = count + 1
            bot.register_next_step_handler(msg, process_find, number, c)
        elif int(user_number) < number:
            msg = bot.reply_to(message, 'Указанное вами число меньше загаданного.')
            c = count + 1
            bot.register_next_step_handler(msg, process_find, number, c)
        else: 
            c = count
            bot.reply_to(message, f'Вы отгадали число за {c} раз!\nЕсли хочешь сыграть ещё раз, запусти игру командой /start.')
            return
            # msg = bot.reply_to(message, 'Всё.\nЕсли хочешь сыграть ещё раз, запусти игру командой /start.')
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так. Перезапусте бот командой /start.\nОшибка: {e}')
#     if user_number == number:
#         msg = bot.reply_to(message, f'Вы отгадали число за {count} раз!')
#         bot.register_next_step_handler(msg, process_end)
#     else:
#         msg = bot.reply_to(message, 'Указанное вами число больше загаданного.')
#         count = count + 1
#         bot.register_next_step_handler(msg, process_age_step)
#         return

def process_find(message, number, count):
    try:
        print(message)
        user_number = message.text
        if not user_number.isdigit():
            msg = bot.reply_to(message, 'Вы указали не число.\nВведите число от 1 до 1000.')
            bot.register_next_step_handler(msg, process_is_digits, number, count)
            return
        elif int(user_number) > number:
            msg = bot.reply_to(message, 'Указанное вами число больше загаданного.')
            c = count + 1
            bot.register_next_step_handler(msg, process_find, number, c)
        elif int(user_number) < number:
            msg = bot.reply_to(message, 'Указанное вами число меньше загаданного.')
            c = count + 1
            bot.register_next_step_handler(msg, process_find, number, c)
        else: 
            c = count + 1
            bot.reply_to(message, f'Вы отгадали число за {c} раз!\nЕсли хочешь сыграть ещё раз, запусти игру командой /start.')
            return
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так. Перезапусте бот командой /start.\nОшибка: {e}')

    #     msg = bot.reply_to(message, 'Указанное вами число больше загаданного.')
    #     count = count + 1
    #     bot.register_next_step_handler(msg, process_age_step)
    #     return count
    # else:
    #     msg = bot.reply_to(message, 'Указанное вами число меньше загаданного.')
    #     count = count + 1
    #     bot.register_next_step_handler(msg, process_age_step)
    #     return count

#     # return count

# def process_end(message):
#     bot.reply_to(message, f'Вы отгадали число за {count} раз!')




# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.infinity_polling()