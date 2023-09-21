import telepot
import time
from Config import TOKEN
from telepot.loop import MessageLoop
from googletrans import Translator

# Init translator
translator = Translator()

# Translate function
def handler(msg):
    msgType, chtType, chatId = telepot.glance(msg)
    message = msg['text']

    try:
        # The bot's startup message
        if message[0:6] == "/start":
            bot.sendMessage (chatId, "Welcome! I am the bot Translator\n\n" \
                "If you want to translate a text into English, please write\n" \
                "To En: and the text you want to translate\n\n" \
                "If you want to translate a text into Spanish, please write\n" \
                "To Es: and the text you want to translate\n\n" \
                "The others lenguages are:\n" \
                "Ukranian To Uk:\n" \
                "French To Fr:\n" \
                "Russian To Ru:\n" \
                "Italian To It:\n\n" \
                "For example,\n" \
                "To Es: Hi. How are you? \n" \
                "I will return\n" \
                "Hola. ¿Cómo estas?")
        
        # Lenguages to translate
        if message[0:6] == "To En:":
            translation = translator.translate(message[6:],dest = 'en')
            bot.sendMessage(chatId,translation.text)
        
        elif message[0:6] == "To Es:":
            translation = translator.translate(message[6:],dest = 'es')
            bot.sendMessage(chatId,translation.text)
        
        elif message[0:6] == "To Uk:":
            translation = translator.translate(message[6:],dest = 'uk')
            bot.sendMessage(chatId,translation.text)
        
        elif message[0:6] == "To Ru:":
            translation = translator.translate(message[6:],dest = 'ru')
            bot.sendMessage(chatId,translation.text)

        elif message[0:6] == "To Fr:":
            translation = translator.translate(message[6:],dest = 'fr')
            bot.sendMessage(chatId,translation.text)

        elif message[0:6] == "To It:":
            translation = translator.translate(message[6:],dest = 'it')
            bot.sendMessage(chatId,translation.text)

    except Exception as error:
        print(f"The error is: {error}")

# Token ID from config file
bot = telepot.Bot(TOKEN)      

MessageLoop(bot,handler).run_as_thread()

while True:
    time.sleep(10)
