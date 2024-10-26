import telebot
import os, random

bot = telebot.TeleBot('Свой токен тут')

@bot.message_handler(commands=['help'])
def help_command(message):
    welcome_text = (
        "Привет! Я бот, который может:\n"
        "1. Отправлять мемы с помощью команды /meme\n"
        "2. Делать интересные факты с помощью команды /facts\n"
        "Используйте команды, чтобы взаимодействовать со мной!"
    )
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['meme'])
def send_meme(message):
    img_name = random.choice(os.listdir("img"))
    with open(f"img/{img_name}", "rb") as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands = ["facts"])
def facts(message):
    facts_random = ["Каждый год исчезает около 10 000 видов животных и растений",
                    "Каждый год в океан попадает около 8 миллионов тонн пластика.",
                     "Температура на Земле увеличилась на 1,1°C с конца 19 века, что вызывает экстремальные погодные условия."]
    random_fact = random.choice(facts_random)  
    bot.send_message(message.chat.id, random_fact)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Используй команду /mem, чтобы получить мем!")



bot.polling()


































