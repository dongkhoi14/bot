from dotenv import load_dotenv
import os
import telebot
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
print(BOT_TOKEN)