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
                "If you want to translate a text into other languages, please write\n\n" \
                "To Es: to translate into Spanish\n" \
                "To Uk: to translate into Ukranian\n" \
                "To Fr: to translate into French\n" \
                "To De: to translate into German\n" \
                "To Ru: to translate into Russian\n" \
                "To It: to translate into Italian\n\n" \
                "For example,\n" \
                "To Es: Hi. How are you? \n" \
                "I will return\n" \
                "Hola. ¿Cómo estas?")
        
        # Languages list
        # If you want to add more languages, you can check them at the following link
        # https://gist.github.com/ivansaul/97058b5c07431911427db68bcbdbc92c
        langs_list=['To En:', 'To Es:', 'To Uk:', 'To Fr:', 'To De:', 'To Ru:', 'To It:']

        # Variables to validate the language to be translate
        conv_lower = map(lambda x: x.lower(), langs_list)
        lang_list_lower = list(conv_lower)
        val_lang = message[0:6].lower()
        new_lang = val_lang[-3:-1]
        items = '\n'.join(map(str, langs_list))

        # Languages to translate
        if val_lang in lang_list_lower:
            translation = translator.translate(message[6:], dest = new_lang)
            bot.sendMessage(chatId, translation.text)

        else:
            new_message = f"Remember. I can't translate if you don't first write the lenguage you want to translate \n{items}"
            bot.sendMessage(chatId, new_message)

    except Exception as error:
        print(f"The error is: {error}")

# Token ID from config file
bot = telepot.Bot(TOKEN)      

MessageLoop(bot,handler).run_as_thread()

while True:
    time.sleep(10)
