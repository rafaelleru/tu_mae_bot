import telebot
import os

bot = telebot.TeleBot(os.environ["tu_mae_token"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "/tumae")

def recibe(messages):
    for m in messages:
        if m.chat.type == 'group' or m.chat.type == 'supergroup':
            if m.from_user.username == 'SRMarin':
                bot.send_message(m.chat.id, 'Comprate un cuello sirolo')
            elif m.from_user.username == 'Raulytaso':
                bot.send_message(m.chat.id, 'Subete los pantalones mierda')
            elif m.from_user.username == 'McMayXIII':
                bot.send_message(m.chat.id, 'Porreroooo')
                
            if m.content_type == 'text':
                if 'quien' in m.text or 'Quien' in m.text:
                    bot.send_message(m.chat.id, '/tumae')
                elif '/spam' in m.text:
                    for i in range (0, 10):
                        bot.send_message(m.chat.id, '/spam')
        #fin del if
        else:
            bot.send_message(m.chat.id, "tus muertos siroloooooooo")

bot.set_update_listener(recibe)
bot.polling()
