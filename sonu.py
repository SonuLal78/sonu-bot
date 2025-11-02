import threading
import time
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# कॉन्फ़िगरेशन
TOKEN = '7691204061:AAEQNdpJmPf1S1w2vxOBid-fpH4Az3Nkro0'
DATA_FILE = 'config.json'

# डेटा लोड या इनिशियलाइज़ करना
try:
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"ip": "", "port": "", "duration": 0}

# /start कमांड का हैंडलर
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome To Sonu Lal bot")

# IP, Port, Duration सेट करने का तरीका
def set_config(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /set ip port duration")
        return
    ip, port, duration = args
    global data
    data = {
        "ip": ip,
        "port": port,
        "duration": int(duration)
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
    update.message.reply_text("Configuration Saved!")

# बॉट को हाई बफर, थ्रेड्स और टाइमर के साथ रन करना
def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("set", set_config))
    updater.start_polling()
    updater.idle()

# मुख्य फंक्शन
if __name__ == "__main__":
    # थ्रेड्स का उपयोग कर बॉट चलाएँ
    for _ in range(100):
        threading.Thread(target=run_bot).start()

    # 600 सेकंड तक चलने का टाइमर
    time.sleep(600)
    print("Bot stopped after 600 seconds.")
