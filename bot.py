import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("سلام! ربات با موفقیت اجرا شد.")

TOKEN = os.environ.get("BOT_TOKEN")
updater = Updater(token=TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
