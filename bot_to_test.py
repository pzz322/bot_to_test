import telebot
from time import sleep
from threading import Thread


API_TOKEN = "API_TOKEN"

bot = telebot.TeleBot(API_TOKEN)
admins = [12384, 77754]

@bot.message_handler(commands=['send'])
def notify(message):
    command_sender = message.from_user.id
    if command_sender in admins:
        with open(r'/path/to/file/chat.txt') as ids:
            for line in ids:
                user_id = int(line.strip("\n"))
                try:
                    bot.send_message(user_id,  f'message t {command_sender}')
                except Exception as e:
                    bot.send_message(command_sender, f'error sending message - {user_id}')
    else:
        bot.send_message(command_sender, f'Not enough rights')


if __name__ == "__main__":
    try:
        Thread(target = bot.polling(none_stop=True)).start()
        while True:
            sleep(1800)
            Thread(target = bot.polling(none_stop=True)).start()
    except Exception as e:
        pass