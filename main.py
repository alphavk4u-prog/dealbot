import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from keep_alive import keep_alive

keep_alive()

TOKEN = os.getenv("8603385166:AAErpTV-TjEdvznd_RWOmvt_N4hLzpMN-CE")
bot = telebot.TeleBot(TOKEN)

subscribers = []

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🛒 Deals by App", callback_data="apps"),
        InlineKeyboardButton("⚡ Quick Deals", callback_data="loot")
    )
    markup.row(
        InlineKeyboardButton("🎯 Best Deals", callback_data="best"),
        InlineKeyboardButton("🔔 Subscribe", callback_data="sub")
    )

    bot.send_message(message.chat.id,
    "🔥 Welcome to DealKhojo Bot\n\n"
    "💸 Paisa bachao, best deals pao 😄",
    reply_markup=markup)

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
        bot.send_message(call.message.chat.id,
        "🔥 Amazon Deals:\n\n"
        "🎧 Headphones ₹1499\n"
        "🔗 https://amzn.to/example")

    elif call.data == "flipkart":
        bot.send_message(call.message.chat.id,
        "🔥 Flipkart Deals:\n\n"
        "⌚ Smartwatch ₹1999\n"
        "🔗 https://fkrt.in/example")

    elif call.data == "myntra":
        bot.send_message(call.message.chat.id,
        "🔥 Myntra Deals:\n\n"
        "👕 T-shirt ₹299\n"
        "🔗 https://myntra.com/example")

    elif call.data == "meesho":
        bot.send_message(call.message.chat.id,
        "🔥 Meesho Deals:\n\n"
        "👜 Bag ₹399\n"
        "🔗 https://meesho.com/example")

    elif call.data == "loot":
        bot.send_message(call.message.chat.id,
        "⚡ QUICK LOOT DEAL 🔥\n\n"
        "💥 Product ₹99\n"
        "⏳ Limited Time")

    elif call.data == "best":
        bot.send_message(call.message.chat.id,
        "🎯 Today’s Best Deals:\n\n"
        "1. Headphones ₹1499\n"
        "2. Shoes ₹999")

    elif call.data == "sub":
        user_id = call.message.chat.id
        if user_id not in subscribers:
            subscribers.append(user_id)
            bot.send_message(user_id, "✅ Subscribed!")
        else:
            bot.send_message(user_id, "⚡ Already subscribed!")

print("Bot chal raha hai...")
bot.polling()
