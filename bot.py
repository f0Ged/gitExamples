import telebot

bot = telebot.TeleBot(1218687025:AAENfVHuk-yV4zGCdvndRDJjm63ebm9psCc)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Macibas! 🖐
Я ждала тебя, так ждала!Классно, что ты мне пишешь! 
Мы уже знакомы, я Елена Истомина, маркетолог с очаровательной улыбкой и глубокими знаниями в таргетированной рекламе. Слышала, ты тоже держишь нос по ветру, предлагаю посоревноваться, спорим, я тебя сделаю? 

Если правильно ответишь на все вопросы, получишь бонус от меня 

П.С. захочешь попрощаться – напиши /off')


if __name__ == '__main__':
    bot.polling(none_stop=True)