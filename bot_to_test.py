import telebot
from time import sleep

API_TOKEN = "API_TOKEN"

bot = telebot.TeleBot(API_TOKEN)

def notify(message):
    command_sender = message.from_user.id
    with open(r'/path/to/file/chat.txt') as ids:
        while True:        
            for line in ids:
                user_id = int(line.strip("\n"))
                try:
                    bot.send_message(user_id,  f'message to {command_sender}')
                except Exception as e:
                    bot.send_message(command_sender, f'error sending message - {user_id}')
                sleep(1800)
        else:
            bot.send_message(command_sender, f'Not enough rights')


if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass
