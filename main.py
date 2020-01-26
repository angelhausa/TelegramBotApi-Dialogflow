import apiai
import json
import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, ")

@bot.message_handler(content_types=['text'])
def textMessage(message):
    request = apiai.ApiAI('Token_Dialogflow').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'session_id' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял

    if response:
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, text='Я Вас не совсем понял!')


#def smail(message):
#    if:
#        pass
#    else:
#        pass


if __name__ == '__main__':
     bot.polling(none_stop=True)


