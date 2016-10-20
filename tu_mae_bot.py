import telebot
import os
import random
import logging

bot = telebot.TeleBot(os.environ["tu_mae_token"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "/tumae")

def recibe(messages):
    for m in messages:
        if m.chat.type == 'group' or m.chat.type == 'supergroup':
            ran = random.randint(1, 9)

            if ran < 3:
                if m.from_user.username == 'SRMarin':
                    bot.send_message(m.chat.id, 'Comprate un cuello sirolo')
                elif m.from_user.username == 'Raulytaso':
                    bot.send_message(m.chat.id, 'Subete los pantalones mierda')
                elif m.from_user.username == 'McMayXIII':
                    bot.send_message(m.chat.id, 'Porreroooo')

            ran = random.randint(1,20)

            if m.content_type == 'text' and ran < 4:
                if 'quien' in m.text or 'Quien' in m.text:
                    if(ran==1):
                        bot.send_message(m.chat.id, '/lamaedelsergio')
                    else:
                        bot.send_message(m.chat.id, '/tumae')
                if 'cafeto' in m.text:
                    if(ran==1):
                        bot.send_message(m.chat.id, '/lamaedelsergio')
                    else:
                        bot.send_message(m.chat.id, '/tumae')
                if 'cafeteria' in m.text:
                    if(ran==1):
                        bot.send_message(m.chat.id, '/lamaedelsergio')
                    else:
                        bot.send_message(m.chat.id, '/tumae')
#            if m.content_type == 'text':
#               if '/spam' in m.text:
#                   for i in range (0, 10):
#                        bot.send_message(m.chat.id, '/spam')

            ran = random.randint(1,200)
            if(ran==2):
                import urllib
                ran1 = random.randint(100, 500)
                ran2 = random.randint(1, 3)
                f = open('1.jpg', 'wb')
                if(ran2==1):
                    f.write(urllib.urlopen('https://www.placecage.com/'+ran1+'/'+ran1).read())
                if(ran2==2):
                    f.write(urllib.urlopen('https://www.placecage.com/g/'+ran1+'/'+ran1).read())
                if(ran2==3):
                    f.write(urllib.urlopen('https://www.placecage.com/c/'+ran1+'/'+ran1).read())
                f.close()

                photo = open('1.jpg', 'rb')
                bot.send_photo(m.chat.id,photo)

        else:
            bot.send_message(m.chat.id, "tus muertos siroloooooooo")

bot.set_update_listener(recibe)
bot.polling(none_stop=False)
