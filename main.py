import telebot
from logic import *
from config import *
import config
bot = telebot.TeleBot(config.API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
команды:/otvet\
""")

@bot.message_handler(commands=['found'])
def foundquestion(message):
    try:
        id = found(message.text[7:])
        answer = found_answer(id)
        bot.reply_to(message,answer)
    except:
        bot.reply_to(message,'такого вопроса не нашлось попробуйте проверить правельность написания вопроса')
    
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text in config.questions.keys():
        bot.reply_to(message,config.questions[message.text])
    else:
        bot.reply_to(message,'ответа на данный вопрос нет обратитесь в тех поддержку')
        add_question(message.text)
bot.infinity_polling()