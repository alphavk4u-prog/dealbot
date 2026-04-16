import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time
import threading
from keep_alive import keep_alive

keep_alive()

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

subscribers = []

MAIN_CHANNEL = "@DealKhojo4u"

# START MENU
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🛒 Deals by App", callback_data="apps"),
        InlineKeyboardButton("⚡ Quick Deals", callback_data="loot")
    )
    markup.row(
        InlineKeyboardButton("🎯 Best Deals", callback_data="best"),
        InlineKeyboardButton("🔥 Flash Deals", callback_data="flash")
    )
    markup.row(
        InlineKeyboardButton("🔔 Subscribe", callback_data="sub"),
        InlineKeyboardButton("📢 Join & Links", callback_data="links")
    )

    bot.send_message(message.chat.id,
    "🔥 Welcome to DealKhojo Bot\n\n"
    "💸 Sabse fast deals yahi milenge\n"
    "⏳ 2 min me deal khatam ho sakti hai!",
    reply_markup=markup)

# BUTTON HANDLER
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "apps":
        markup = InlineKeyboardMarkup()
        markup.row(
            InlineKeyboardButton("Amazon", callback_data="amazon"),
            InlineKeyboardButton("Flipkart", callback_data="flipkart")
        )
        markup.row(
            InlineKeyboardButton("Myntra", callback_data="myntra"),
            InlineKeyboardButton("Meesho", callback_data="meesho")
        )
        bot.send_message(call.message.chat.id, "🛒 Select App:", reply_markup=markup)

    elif call.data == "amazon":
        bot.send_message(call.message.chat.id, "🛒 Amazon Deals\nJoin channel for latest 👇\nhttps://t.me/DealKhojo4u")

    elif call.data == "flipkart":
        bot.send_message(call.message.chat.id, "🛍️ Flipkart Deals\nJoin channel 👇\nhttps://t.me/DealKhojo4u")

    elif call.data == "myntra":
        bot.send_message(call.message.chat.id, "👕 Myntra Deals\nJoin channel 👇\nhttps://t.me/DealKhojo4u")

    elif call.data == "meesho":
        bot.send_message(call.message.chat.id, "📦 Meesho Deals\nJoin channel 👇\nhttps://t.me/DealKhojo4u")

    elif call.data == "loot":
        bot.send_message(call.message.chat.id,
        "⚡ LOOT DEALS 🔥\n\n"
        "⏳ Ye deals seconds me khatam hoti hain!\n"
        "👉 Join karo fast 👇\nhttps://t.me/DealKhojo4u")

    elif call.data == "flash":
        bot.send_message(call.message.chat.id,
        "🔥 FLASH DEALS ⚡\n\n"
        "⏳ 2 min me khatam ho sakti hai!\n"
        "👉 Abhi join karo 👇\nhttps://t.me/DealKhojo4u")

    elif call.data == "best":
        bot.send_message(call.message.chat.id,
        "🎯 Best Deals Today 🔥\n\n"
        "👉 Sabse top deals yaha milengi\n"
        "👇 Join Now\nhttps://t.me/DealKhojo4u")

    elif call.data == "sub":
        user_id = call.message.chat.id
        if user_id not in subscribers:
            subscribers.append(user_id)
            bot.send_message(user_id, "✅ Subscribed!\n⚡ Ab tumhe sabse fast deals milengi")
        else:
            bot.send_message(user_id, "⚡ Already subscribed")

    elif call.data == "links":
        bot.send_message(call.message.chat.id,
        "📢 DealKhojo Network\n\n"
        "👉 Main Channel: https://t.me/DealKhojo4u\n"
        "👉 Backup Channel: https://t.me/OffersDealKhojo\n"
        "👉 Instagram: https://instagram.com/Vishalvk4u\n\n"
        "🔥 Sab join karo warna deal miss ho jayegi!")

# AUTO DEAL SYSTEM
def auto_send():
    while True:
        message = (
            "🔥 AUTO DEAL ALERT 🔥\n\n"
            "⏳ 2 min me khatam ho sakta hai!\n"
            "👉 Fast join karo👇\nhttps://t.me/DealKhojo4u"
        )

        for user in subscribers:
            try:
                bot.send_message(user, message)
            except:
                pass

        time.sleep(60)

threading.Thread(target=auto_send).start()

print("Bot chal raha hai...")
bot.polling()
