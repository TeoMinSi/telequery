import os
import sys
from threading import Thread
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler, BaseFilter, CallbackQueryHandler
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove
import telegram
import re
import requests 


# DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

PORT = os.environ.get('PORT')
#sean token
#TOKEN = "1009109451:AAGDSNMbSGloAUoCW9EYTlEUf1vMMuhrnZc"
#ms token
TOKEN = '815123050:AAGYmp4G3WQRs2DkGBlyCfedF7yIJXKGH9A'
NAME = "msflasktele"
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
base_url = 'https://{}.herokuapp.com/'.format(NAME)
query_test = base_url + "query_test/"
query_app_name = "mstelequery"

def start(update, context):
    update.effective_message.reply_text("Where is the location you would like to query?")


def reply(update, context):
	print(update.effective_message.text)
	payload = {"name":update.effective_message.text, "timestamp":time.timenow()}
	r = requests.get(query_test, json=payload)
	print(r.status_code)
	print(r.text)
	if r.status_code == 201:
		update.effective_message.reply_text(r.json()["result"])		
# def test(update, context):

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, reply))

updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(query_app_name, TOKEN))
updater.idle()