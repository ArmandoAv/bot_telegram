######################################
# This file can take a Token ID from #
# a file or an environment variable  #
######################################

import telepot
import time
# Token ID from environment variable
import os
# Token ID from config file
#from Config import TOKEN
from telepot.loop import MessageLoop
from googletrans import Translator

# Init translator
translator = Translator()

# Translate function
def handler(msg):
    msgType, chtType, chatId = telepot.glance(msg)
    message = msg['text']

    try:
        # Languages description list
        # If you want to add more languages, you must add them here 
        # You can check others languages at the following link
        # https://gist.github.com/ivansaul/97058b5c07431911427db68bcbdbc92c
        # If you want to add Japanese you have to look for its ASCII code
        # in this case it's 'ja' so it must be added to the list the new item
        # 'To Ja: and text to translate into Japanese',
        desc_lang = [
                        'To Es: and text to translate into Spanish',
                        'To Uk: and text to translate into Ukranian',
                        'To Fr: and text to translate into French',
                        'To De: and text to translate into German',
                        'To Ru: and text to translate into Russian',
                        'To It: and text to translate into Italian',
                    ]

        # Display the list in several lines
        desc_lang_items = '\n'.join(map(str, desc_lang))

        # Create language list from languages description list
        # This list contains the commands to translate in the telegram bot
        # 'To En:', 'To Es:', ..., 'To It:' 
        langs_list=['To En:']

        for i in range(len(desc_lang)):
            langs_list.append(desc_lang[i][0:6])

        # Variables to validate the language to be translate
        conv_lower = map(lambda x: x.lower(), langs_list)
        lang_list_lower = list(conv_lower)
        val_lang = message[0:6].lower()
        new_lang = val_lang[-3:-1]
        items = '\n'.join(map(str, langs_list))

        # The bot's startup message
        if val_lang == "/start":
            bot.sendMessage (chatId, "Welcome! I am a bot Translator\n\n" \
                "If you want to translate a text into English, please write\n\n" \
                "To En: and the text you want to translate\n\n" \
                "If you want to translate a text into other languages, please write\n\n" \
               f"{desc_lang_items}" \
                "\n\nFor example, if you write\n" \
                "To Es: Hi. How are you? \n" \
                "I will return\n" \
                "Hola. ¿Cómo estás?")

        # Languages to translate
        elif val_lang in lang_list_lower:
            translation = translator.translate(message[6:], dest = new_lang)
            bot.sendMessage(chatId, translation.text)

        else:
            new_message = "Remember. I can't translate if you don't first " \
                          "write the language you want to translate \n" \
                         f"{items}" \
                          "\n\nIf you need to see the descriptions again " \
                          "just type \n" \
                          "/start"
            bot.sendMessage(chatId, new_message)

    except Exception as error:
        print(f"The error is: {error}")

# Token ID from environment variable
token = os.environ.get('TOKEN')
bot = telepot.Bot(token)

# Token ID from Config file
#bot = telepot.Bot(TOKEN)

# Running the bot
MessageLoop(bot, handler).run_as_thread()

while True:
    time.sleep(10)
