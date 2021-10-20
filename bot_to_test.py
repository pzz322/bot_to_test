from time import sleep
from telethon.sync import TelegramClient
 
api_id = 'ID_BOT'
api_hash = 'HASH'
bot_token = 'API TOKEN'

def send(text):
    with TelegramClient('Session', api_id, api_hash).start(bot_token=bot_token) as client:
        command_sender = text.from_user.id
        with open(r'/path/to/file/chat.txt') as ids:
            while True:        
                for line in ids:
                    user_id = int(line.strip("\n"))
                    try:
                        client.send_message(user_id,  f'message to {command_sender}')
                    except Exception as e:
                        client.send_message(command_sender, f'error sending message - {user_id}')
                sleep(1800)
            else:
                client.send_message(command_sender, f'Not enough rights')
        client.run_until_disconnected()
 
if __name__ == '__main__':
    text = input('Enter text ')
    send(text)
