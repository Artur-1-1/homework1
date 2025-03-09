import telebot

TOKEN = '7237082682:AAF2OxYfftKvVIbg_Nc7tCJCV62AVSA01FU'  # Вставте токен, який надіслав BotFather
bot = telebot.TeleBot(TOKEN)

chat_id = 5064742315  # Введи ID чату (@userinfobot)

def convert_unit(value, from_units, to_units):
    conversions = {
        "сантиметр": {"міліметри": 10},
        "дициметр": {"міліметри": 100},
        "метр": {"міліметри": 1000},
        "кілометр": {"міліметри": 1000000},
        "літр": {"мілілітри": 1000},
        "кілограм": {"грами": 1000},
        "центнер": {"грами": 100000},
        "тонна": {"грами": 1000000}
    }
    
    if from_units in conversions and to_units in conversions[from_units]:
        return value * conversions[from_units][to_units]
    else:
        return None

@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Привіт мій маленький друже! Я допоможу тобі вивчити - кількість міліметрів, мілілітрів і грам в більших величинах.\n"
                                      "Напиши в такому форматі: 5 метр в міліметри.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    try:
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]

        value = float(value_and_from_unit[0])
        from_unit = " ".join(value_and_from_unit[1:])

        result = convert_unit(value, from_unit, to_unit)
        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id, "Не можу конвертувати, спробуйте ще раз.")
    except Exception as e:
        bot.send_message(message.chat.id, "Все погано, у тебе помилка в коді.")

bot.polling()